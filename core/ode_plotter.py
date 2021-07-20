# from mpl_toolkits import mplot3d
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from math import hypot
matplotlib.use('Agg')


class OdePlotter:

    def __init__(self, c):
        self.__case = c

    def three_d_plot(self, _dict):
        figure = plt.figure(figsize=(10, 10))
        figure.suptitle(self.__case + ": 3d Plot", fontsize=20, fontweight='bold')
        ax = plt.axes(projection="3d")

        x = _dict['x_val']
        y = _dict['y_val']
        z = _dict['z_val']

        ax.plot(x, y, z, linewidth=1)

        # Setting the labels for axis
        ax.set_xlabel('x-axis')
        ax.set_ylabel('y-axis')
        ax.set_zlabel('z-axis')
        return figure

    def three_d_plot_color(self, _dict):
        figure = plt.figure(figsize=(10, 10))
        figure.suptitle(self.__case + ": 3d Plot with colors", fontsize=20, fontweight='bold')
        ax = plt.axes(projection="3d")

        x = _dict['x_val']
        y = _dict['y_val']
        z = _dict['z_val']
        N = len(x)

        dists = []

        # Calculating distance between xyz values and saving them in a list
        for i in range(N - 1):
            a = np.array((x[i], y[i], z[i]))
            b = np.array((x[i + 1], y[i + 1], z[i + 1]))
            dist = np.linalg.norm(a - b)
            dists.append(dist)

        # Calculating the maximum distance in a list of distances (for normalization)
        max_val = max(dists)

        # For each point-pair, plot the line with color depending on the distance
        for i in range(N - 1):
            dist = dists[i]
            rgb_to_deduct = dist / max_val
            c = (0.3, 1 - rgb_to_deduct, 0.7)
            ax.plot(x[i:i + 2], y[i:i + 2], z[i:i + 2], color=c, linewidth=1)

        # Setting the labels for axis
        ax.set_xlabel('x-axis')
        ax.set_ylabel('y-axis')
        ax.set_zlabel('z-axis')
        return figure

    def two_d_plot(self, _dict, plot_axes):
        figure = plt.figure(figsize=(10, 10))
        figure.suptitle(self.__case + ": 2D Plot on " + str(plot_axes) + " axes", fontsize=20, fontweight='bold')
        if plot_axes == 'xy':
            a_coordinates = _dict['x_val']
            b_coordinates = _dict['y_val']
            x_axis_label = 'x-axis'
            y_axis_label = 'y-axis'
        elif plot_axes == 'yz':
            a_coordinates = _dict['y_val']
            b_coordinates = _dict['z_val']
            x_axis_label = 'y-axis'
            y_axis_label = 'z-axis'
        elif plot_axes == 'xz':
            a_coordinates = _dict['x_val']
            b_coordinates = _dict['z_val']
            x_axis_label = 'x-axis'
            y_axis_label = 'z-axis'
        else:
            return

        plt.plot(a_coordinates, b_coordinates, linewidth=1)

        # Setting the labels for axis
        plt.xlabel(x_axis_label)
        plt.ylabel(y_axis_label)
        return figure

    def two_d_plot_color(self, _dict, plot_axes):
        figure = plt.figure(figsize=(10, 10))
        figure.suptitle(self.__case + ": 2D Plot with colors on " + str(plot_axes) + " axes", fontsize=20, fontweight='bold')

        if plot_axes == 'xy':
            a_coordinates = _dict['x_val']
            b_coordinates = _dict['y_val']
            x_axis_label = 'x-axis'
            y_axis_label = 'y-axis'
        elif plot_axes == 'yz':
            a_coordinates = _dict['y_val']
            b_coordinates = _dict['z_val']
            x_axis_label = 'y-axis'
            y_axis_label = 'z-axis'
        elif plot_axes == 'xz':
            a_coordinates = _dict['x_val']
            b_coordinates = _dict['z_val']
            x_axis_label = 'x-axis'
            y_axis_label = 'z-axis'
        else:
            return

        N = len(a_coordinates)

        dists = []

        # Calculate distances between points and put them in a list
        for i in range(N - 1):
            a = [a_coordinates[i], b_coordinates[i]]
            b = [a_coordinates[i + 1], b_coordinates[i + 1]]
            dist = hypot(a[0] - b[0], a[1] - b[1])
            dists.append(dist)

        # Calculate the maximum distance (used for normalization)
        max_val = max(dists)

        # For each point-pair, plot the line with color depending on the distance
        for i in range(N - 1):
            dist = dists[i]
            rgb_to_deduct = dist / max_val
            c = (0.3, 1 - rgb_to_deduct, 0.7)
            plt.plot(a_coordinates[i:i + 2], b_coordinates[i:i + 2], color=c, linewidth=1)

        # Setting the labels for axis
        plt.xlabel(x_axis_label)
        plt.ylabel(y_axis_label)
        return figure
