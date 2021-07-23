#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Definition of class OdeFileHandler
@author: kashifrabbani@cs.aau.dk
@author: imranh@cs.aau.dk
"""


class OdeFileHandler:

    def __init__(self, d):
        self.__directory = d

    def ode_solver_writer(self, s, filename):
        f = open(self.__directory + filename, "w")
        f.write(s)
        f.close()

    def ode_solver_reader(self):
        pass

    def ode_data_writer(self, d, filename):
        f = open(self.__directory + filename, "w")
        # Writing each value in a different line in CSV syntax
        for i in range(0, len(d['x_val'])):
            f.write(str(d['x_val'][i]) + ";" + str(d['y_val'][i]) + ";" + str(d['z_val'][i]) + "\n")
        f.close()

    def ode_data_reader(self):
        pass

    def ode_plot_figure_saver(self, fig, filename):
        fig.savefig(self.__directory + filename, bbox_inches='tight')
