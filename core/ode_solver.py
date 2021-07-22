#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Definition of class OdeSolver
@author: kashifrabbani@cs.aau.dk
@author: imranh@cs.aau.dk
"""


class OdeSolver:
    """
    OdeSolver class simulates a solution for Lorenz Attractor Ordinary Differential Equation Solver using Euler
    approximation approach provided a set of variable values and initial values for x,y,z.
    """
    __time_interval = 0.02
    __num_of_steps = 10000

    def __init__(self, sigma_val, beta_val, rho_val):
        """
        Constructor to set the value for arguments sigma (argument 1), beta (argument 2), and rho (argument 3).
        """
        self.__sigma = sigma_val
        self.__beta = beta_val
        self.__rho = rho_val

    def set_time_interval(self, t):
        """
        Set the value for the t_delta
        """
        self.__time_interval = t

    def set_num_of_steps(self, steps):
        """
        Set the number of time steps to arg1
        """
        self.__num_of_steps = steps

    def get_time_interval(self):
        """
        Return time interval
        """
        return self.__time_interval

    def get_num_of_steps(self):
        """
        Return the value of num_of_steps
        """
        return self.__num_of_steps

    def __compute_x(self, x, y):
        """
        Compute a new value of x using given values of x and y. Reference equation 6
        """
        return (self.__sigma * (y - x)) * self.__time_interval + x

    def __compute_y(self, x, y, z):
        """
         Compute a new value of y using given values of x, y, and z. Reference equation 8
        """
        return (x * (self.__rho - z) - y) * self.__time_interval + y

    def __compute_z(self, x, y, z):
        """
         Compute a new value of z using given values of x, y, and z. Reference equation 10
        """
        return (x * y - self.__beta * z) * self.__time_interval + z

    def simulator(self, x_init, y_init, z_init):
        """
        This function works in an iterative way and computes the new values of x, y, and z using euler
        approximation for N number of steps and save the new values in a dictionary.
        """
        x_current = x_init
        y_current = y_init
        z_current = z_init

        x_val = [x_current]
        y_val = [y_current]
        z_val = [z_current]

        # Iterate through 1 through N (N=num)
        for _ in range(1, self.__num_of_steps):
            # Calculate new x,y,z values
            x = self.__compute_x(x_current, y_current)
            y = self.__compute_y(x_current, y_current, z_current)
            z = self.__compute_z(x_current, y_current, z_current)

            # Saving new values
            x_val.append(x)
            y_val.append(y)
            z_val.append(z)

            # Assigning current values to new values
            x_current = x
            y_current = y
            z_current = z

        # Saving and returning the dictionary of results
        result = dict()
        result['x_val'] = x_val
        result['y_val'] = y_val
        result['z_val'] = z_val
        return result

    def to_string(self):
        """
        Presenting ode_solver as string
        """
        solver_string = "Sigma = " + str(self.__sigma) + "\nBeta = " + str(self.__beta) + "\nRho = " + str(
            self.__rho) + "\n"

        if self.__time_interval != 0.01:
            solver_string = solver_string + "Time Interval = " + str(self.__time_interval) + "\n"
        if self.__time_interval != 10000:
            solver_string = solver_string + "N = " + str(self.__time_interval)
        return solver_string

