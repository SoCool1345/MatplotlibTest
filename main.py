# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

import numpy as np
import matplotlib as mt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gripspec
import matplotlib.animation as animation

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ffmpegpath = os.path.abspath("D:\\DevProgram\\DevPackage\\ffmpeg-2022-01-03-git-68d0a7e446-full_build\\bin\\ffmpeg.exe")
    mt.rcParams["animation.ffmpeg_path"] = ffmpegpath
    X = np.arange(0, 10, 0.01)  # X shape： (N,)
    Ys = [np.sin(X + k / 10.0) for k in range(100)]  # Ys shape： (k, N)

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))


    def animate(i):
        axes[0].cla()
        axes[0].plot(X, Ys[i])
        axes[0].set_title(f'y = sin(x + {i}/10)')

        axes[1].cla()
        axes[1].hist(Ys[i], bins=50, orientation='horizontal')


    ani = animation.FuncAnimation(fig, animate, frames=50, interval=50,blit=False)#blit=True 只更新变化的点 interval=50 50ms更新1次
    ani.save('matplotlib-animation-hist.gif')
    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
