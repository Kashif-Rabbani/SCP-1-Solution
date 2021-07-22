#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Definition of class OdeSolverTester to test the functionality of OdeSolver class
@author: kashifrabbani@cs.aau.dk
@author: imranh@cs.aau.dk
"""

import sys
sys.path.append('../')
import os
import time
from core import *

sys.path.append('../')
directory = "../result/case5/"

# Create a directory for this case in case it does not exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Initializing objects for file handler and plotter classes
file_handler = ode_filehander.OdeFileHandler(directory)
plotter = ode_plotter.OdePlotter("Case 5")

print("Initiated Case # 5 ...\n")

sol = ode_solver.OdeSolver(14, 13 / 3, 28)
n = 10000
t = 0.02
print("N: " + str(n) + ", Time Interval: " + str(t) + ", and x , y, z = 1")
sol.set_num_of_steps(n)
sol.set_time_interval(t)

print("Simulating...")
st = time.time()
result = sol.simulator(1, 1, 1)
et = time.time()
print("Time elapsed: %0.3f ms" % ((et - st) * 1000.0))

print("Writing...")
st = time.time()
file_handler.ode_solver_writer(sol.to_string(), "ode_solver.txt")
file_handler.ode_data_writer(result, "ode_result.txt")
et = time.time()
print("Time elapsed: %0.3f ms" % ((et - st) * 1000.0))

print("Plotting 3D...")
st = time.time()
plot = plotter.three_d_plot(result)
plot_color = plotter.three_d_plot_color(result)
file_handler.ode_plot_figure_saver(plot, "plot_3d.png")
file_handler.ode_plot_figure_saver(plot_color, "plot_3d_color.png")
et = time.time()
print("Time elapsed: %0.3f ms" % ((et - st) * 1000.0))

print("Plotting 2D - xy...")
st = time.time()
plot = plotter.two_d_plot(result, "xy")
plot_color = plotter.two_d_plot_color(result, "xy")
file_handler.ode_plot_figure_saver(plot, "plot_2d_xy.png")
file_handler.ode_plot_figure_saver(plot_color, "plot_2d_xy_color.png")
et = time.time()
print("Time elapsed: %0.3f ms" % ((et - st) * 1000.0))

print("Plotting 2D - xz...")
st = time.time()
plot = plotter.two_d_plot(result, "xz")
plot_color = plotter.two_d_plot_color(result, "xz")
file_handler.ode_plot_figure_saver(plot, "plot_2d_xz.png")
file_handler.ode_plot_figure_saver(plot_color, "plot_2d_xz_color.png")
et = time.time()
print("Time elapsed: %0.3f ms" % ((et - st) * 1000.0))

print("Plotting 2D - yz...")
st = time.time()
plot = plotter.two_d_plot(result, "yz")
plot_color = plotter.two_d_plot_color(result, "yz")
file_handler.ode_plot_figure_saver(plot, "plot_2d_yz.png")
file_handler.ode_plot_figure_saver(plot_color, "plot_2d_yz_color.png")
et = time.time()
print("Time elapsed: %0.3f ms" % ((et - st) * 1000.0))
