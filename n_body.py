import numpy as np
from vector_class import MassiveBody
import math
import time
import matplotlib.pyplot as plt
from matplotlib import animation as anime
from scatter_graph import plot_path

def dist(i: np.array,j:np.array, main=True) -> float:
    # Returns the distance of i,j
    if main:
        dist_vec:np.array = j.pos() - i.pos()
        norm_sq = 0
        for k in dist_vec:
            norm_sq += k ** 2
        # vector magnitude ^2 == sum(all args^2)
        return math.sqrt(norm_sq)
    else:
        dist_vec:np.array = j.pos_tmp() - i.pos_tmp()
        norm_sq = 0
        for k in dist_vec:
            norm_sq += k ** 2
        # vector magnitude ^2 == sum(all args^2)
        return math.sqrt(norm_sq)

def unit_vec(i:np.array ,j:np.array, main=True) -> np.array:
    # Returns a unit vector in the direction from i --> j
    # vec(ij) = vec(j) - vec(i)
    if main:
        ij:np.array = j.pos() - i.pos()
        unit_ij = ij / (dist(i,j))
        # a_hat (unit vector) = a / norm(a)
        return unit_ij
    else:
        ij:np.array = j.pos_tmp() - i.pos_tmp()
        unit_ij = ij / (dist(i,j))
        # a_hat (unit vector) = a / norm(a)
        return unit_ij

def n_body_eval(bodies: list, dt: float, total_steps: int) -> None:
    # Takes in the list with the bodies (class objects in a list) and numerically
    # Evaluates their position, time and acceleration in subsequent time steps
    # Gravitational constant
    G = 6.67e-11
        
    step = 0
    while step < total_steps:
        # Part 0: Acceleration_ini
        for b_i in bodies: 
            a_i = np.array([0.0 ,0.0])
            for b_j in bodies:
                # Only consider bodies that is not yourself!
                if not(b_i == b_j):
                    # a (due to b_j) = G * m_j / (r_ij)^2
                    a_ij = (G * b_j.mass / (dist(b_i, b_j) ** 2)) * unit_vec(b_i, b_j)
                    a_i += a_ij

            # Inserting initial acceleration into the list        
            b_i.add_acc(a_i)

        # Part 1: Getting the new temp pos
        for b_i in bodies:
            # Pos: s_n+1 (temp) = s_n + v_n * dt
            b_i.add_pos((b_i.pos() + b_i.vel() * dt), main=False)

        # Part 2: Get the intermediate acceleration
        for b_i in bodies: 
            a_i = np.array([0.0 ,0.0])
            for b_j in bodies:
                # Only consider bodies that is not yourself!
                if not(b_i == b_j):
                    # a (due to b_j) = G * m_j / (r_ij)^2
                    # main = false -> take values from the tmp arrays
                    a_ij = (G * b_j.mass / (dist(b_i, b_j, main=False) ** 2)) * unit_vec(b_i, b_j, main=False)
                    a_i += a_ij

            # Inserting initial acceleration into the list (tmp)        
            b_i.add_acc(a_i, main=False)

        # Part 3: Get the next step velocity
        # v_n+1 = v + dt * (a_n + a_n+1) / 2
        for b_i in bodies:
            v_prime = b_i.vel() + dt * (b_i.acc() + b_i.acc_tmp()) / 2
            b_i.add_vel(v_prime) # Adding to the main branch
        
        # Part 4 get new displacements
        # s_n+1 = s_n + dt * (v_n + v_n+1) / 2
        for b_i in bodies:
            s_prime = b_i.pos() + dt * (b_i.vel() + b_i.vel_list[-2]) / 2
            b_i.add_pos(s_prime) # Adding to the main branch

        step += 1

        


if __name__ == '__main__':
    m_e = 6e24
    m_s = 2e30
    au = 1.5e11
    a = MassiveBody(1*m_s, np.array([2e3, 1e3]), np.array([0.0, 0.0]))
    b = MassiveBody(1*m_s, np.array([31e3, 0]), np.array([0 , -1*au]))
    # c = MassiveBody(1*m_e, np.array([41e3, 0]), np.array([0 , -0.6*au]))


    print ("Stars loaded, running function!")
    start_time = time.time()
    n_body_eval([a,b], 10000, 20000)
    end_time = time.time()
    print (f"Function ran success in {round(end_time -start_time, 2)}s")


    # print (a.pos_list)
    plt.axis('equal')
    plot_path(a.pos_list, colour='r')
    plot_path(b.pos_list, colour='g')
    # plot_path(c.pos_list, colour='b')
    plt.grid(visible=True)

    plt.show()

    # # # create the figure and axes objects
    # fig, ax = plt.subplots()

    # def animate(i):
    #     plt.grid(visible=True)
    #     # ax.clear()
    #     # a_x = []
    #     # a_y = []
    #     # b_x = []
    #     # b_y = []
    #     # for k in range(10):
    #     #     new_xa = a.pos_list[i+k][0]
    #     #     new_ya = a.pos_list[i+k][1]
    #     #     a_x.append(new_xa)
    #     #     a_y.append(new_ya)

    #     #     new_xb = b.pos_list[i+k][0]
    #     #     new_yb = b.pos_list[i+k][1]
    #     #     b_x.append(new_xb)
    #     #     b_y.append(new_yb)
    #     ax.scatter(a.pos_list[i][0], a.pos_list[i][1], c='r')  
    #     ax.scatter(b.pos_list[i][0], b.pos_list[i][1], c='b')
    #     print (f'completed frame {i}')
        


    # ani = anime.FuncAnimation(fig, animate, frames=100, interval=10, repeat=False)
    # FFwriter = anime.FFMpegWriter(fps=30)
    # ani.save('animation.gif')
