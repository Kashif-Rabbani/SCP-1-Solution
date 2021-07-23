# from mpl_toolkits import mplot3d
from math import hypot

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('Agg')


class OdePlotter:
    """
      OdePlotter is
      """
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

        # Calculating distance between xyz values
        for i in range(N - 1):
            a = np.array((x[i], y[i], z[i]))
            b = np.array((x[i + 1], y[i + 1], z[i + 1]))
            # Computing norm using numpy.linalg.norm method
            dist = np.linalg.norm(a - b)
            dists.append(dist)

        # Computing the maximum distance for normalization
        max_distance = max(dists)

        # Plotting points based on their distance in a different color
        # Got an idea from an answer to the question given on the stack overflow:
        # https://stackoverflow.com/questions/15617207/line-colour-of-3d-parametric-curve-in-pythons-matplotlib-pyplot
        for i in range(N - 1):
            dist = dists[i]
            ax.plot(x[i:i + 2], y[i:i + 2], z[i:i + 2], color=(0.29, 1 - (dist / max_distance), 0.75), linewidth=1)

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

        # Computing Euclidean distance between points
        for i in range(N - 1):
            a = [a_coordinates[i], b_coordinates[i]]
            b = [a_coordinates[i + 1], b_coordinates[i + 1]]
            # The math.hypot() method returns the Euclidean norm.
            # The Euclidian norm is the distance from the origin to the given coordinates.
            dist = hypot(a[0] - b[0], a[1] - b[1])
            dists.append(dist)

        # Computing the maximum distance for normalization
        max_distance = max(dists)

        # Plotting points based on their distance in a different color
        # Got an idea from an answer to the question given on the stack overflow:
        # https://stackoverflow.com/questions/15617207/line-colour-of-3d-parametric-curve-in-pythons-matplotlib-pyplot
        for i in range(N - 1):
            dist = dists[i]
            plt.plot(a_coordinates[i:i + 2], b_coordinates[i:i + 2], color=(0.29, 1 - (dist / max_distance), 0.75),
                     linewidth=1)

        # Setting the labels for axis
        plt.xlabel(x_axis_label)
        plt.ylabel(y_axis_label)
        return figure
