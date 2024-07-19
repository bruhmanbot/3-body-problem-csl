from matplotlib import pyplot as plt
import numpy as np
from matplotlib import animation as anime

# create lists for the x and y data
t = np.linspace(0,10,100)
x = t
y = (t ** 3 + 3) / (t ** 2 - 4)

# create the figure and axes objects
fig, ax = plt.subplots()

ax.set_xlim([0,11])
ax.set_ylim([-1.1,1.1])

for i in range(100):
    plt.grid(visible=True)
    # ax.clear()
    ax.set_xlim([0,11])
    ax.set_ylim([-10,10])

    ax.plot(x[:i], y[:i], color='k')
    plt.pause(0.0160)

plt.show()
    


# ani = anime.FuncAnimation(fig, animate, frames=500, interval=5, repeat=False)
# FFwriter = anime.FFMpegWriter(fps=50)
# ani.save('animation.gif')

