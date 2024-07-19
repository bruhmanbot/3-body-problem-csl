import matplotlib.pyplot as plt

def plot_path(path:list, style=""):
    x = []
    y = []
    for pos in path:
        x.append(pos[0])
        y.append(pos[1])

    plt.scatter(x, y, fmt=style)