import matplotlib.pyplot as plt
import numpy as np


def plot_path(path:list, colour="", size=0.4):
    x = []
    y = []
    for pos in path:
        x.append(pos[0])
        y.append(pos[1])

    plt.scatter(x, y, c=colour, s=size)

if __name__ == '__main__':
    a1 = np.array([3, 0])
    a2 = np.array([4, 5])
    path1 = [a1, a2]

    b1 = a1 + 5
    b2 = a2 + 10
    path2 = [b1, b2]

    plot_path(path1, colour='b')
    plot_path(path2, colour='r')

    plt.show()