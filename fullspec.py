import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def pic_draw(df, title_name):

    df = np.array(df)
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    # Data for three-dimensional scattered points
    zdata = df[30:, 1:]
    zdata = zdata*1000
    xdata, ydata = np.meshgrid(df[0, 1:], df[30:, 0])
    
    ax.set_xlabel('Time (msec)', fontsize=6)
    ax.set_ylabel('Wavelength (nm)', fontsize=6)
    ax.set_zlabel('Diff. Absorbance (mOD)', fontsize=6)

    g = ax.plot_surface(
        xdata, ydata, zdata, label='HEBR', cmap='rainbow')

    fig.colorbar(g, label='Diff. Ab (mOD)')
    # General view
    ax.view_init(20, -150)
    # Wavelength view
    # ax.view_init(0, 0)
    # Top view
    # ax.view_init(90, -90)
    plt.show()


if __name__ == '__main__':
    import sys
    import os
    input_path = sys.argv[1]
    title_name = ""
    df = pd.read_csv(input_path, skiprows=5, header=None, index_col=None)
    input_path = os.path.splitext(input_path)[0]
    pic_draw(df, title_name)
    # plt.savefig(input_path+".png")
