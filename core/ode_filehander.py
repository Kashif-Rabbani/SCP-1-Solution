#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Definition of class OdeFileHandler
@author: kashifrabbani@cs.aau.dk
@author: imranh@cs.aau.dk
"""


class OdeFileHandler:
    """
    OdeFileHandler class declares standard methods for file read/write operations for our use cases
    """
    def __init__(self, d):
        """
        Constructor to set the value for argument d:directory
        """
        self.__directory = d

    def ode_solver_writer(self, s, filename):
        """
        File writer method to write the given details of ODE solver in the file
        """
        f = open(self.__directory + filename, "w")
        f.write(s)
        f.close()

    def ode_solver_reader(self):
        pass

    def ode_data_writer(self, d, filename):
        """
        File reader method to read the details saved for the specified ODE case
        """
        f = open(self.__directory + filename, "w")
        # Writing each value in a different line in CSV syntax
        for i in range(0, len(d['x_val'])):
            f.write(str(d['x_val'][i]) + ";" + str(d['y_val'][i]) + ";" + str(d['z_val'][i]) + "\n")
        f.close()

    def ode_data_reader(self):
        pass

    def ode_plot_figure_saver(self, fig, filename):
        """
        Figure saver method
        """
        fig.savefig(self.__directory + filename, bbox_inches='tight')
