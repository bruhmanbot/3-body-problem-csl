import numpy as np

class MassiveBody:
    def __init__(self, mass:float, ini_vel:np.array, ini_pos:np.array):
        # Mass (in kg)
        self.mass = mass
        
        # Initialise velocity list (SI Units!)
        self.vel_list = [ini_vel]
        self.vel_list_tmp = []

        # Position (SI Units!)
        self.pos_list = [ini_pos]
        self.pos_list_tmp = []
        

        # Initialise acceleration list
        self.acc_list = []
        self.acc_list_tmp = []



    def add_vel(self, vel:np.array, main=True):
        # Adds a new velocity to the vel_list
        if main:
            self.vel_list.append(vel)
        else:
            self.vel_list_tmp.append(vel)
        return
    
    def add_pos(self, pos:np.array, main=True):
        # Adds a new velocity to the pos_list
        if main:
            self.pos_list.append(pos)
        else:
            self.pos_list_tmp.append(pos)
        return
    
    def add_acc(self, acc:np.array, main=True):
        # Adds a new velocity to the acc_list
        if main:
            self.acc_list.append(acc)
        else:
            self.acc_list_tmp.append(acc)
        return
    
    def vel(self):
        return self.vel_list[-1]
    
    def vel_tmp(self):
        return self.vel_list_tmp[-1]
    
    def pos(self):
        return self.pos_list[-1]
    
    def pos_tmp(self):
        return self.pos_list_tmp[-1]
    
    def acc(self):
        return self.acc_list[-1]
    
    def acc_tmp(self):
        return self.acc_list_tmp[-1]
    
    def __eq__(self, other):
        # Equality
        return (self.mass == other.mass) and (self.pos() == other.pos()).all and (self.vel() == other.vel()).all()

if __name__ == '__main__':
    sun_init_pos = np.array([0,0])
    sun_init_vel = np.array([1e3, 0])
    sun = MassiveBody(2e30, sun_init_vel, sun_init_pos)


    sun.add_vel(np.array([6,0]))
    print(sun.vel_list)
