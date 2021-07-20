#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Definition of class OdeSolverTester to test the functionality of OdeSolver class
@author: kashifrabbani@cs.aau.dk
@author: imranh@cs.aau.dk
"""

import sys
import unittest

import ode_solver

sys.path.append('../')


class OdeSolverTester(unittest.TestCase):
    solver_obj = ode_solver.OdeSolver(1, 2, 3)

    def test_to_initiate_ode_solver(self):
        obj = ode_solver.OdeSolver(1, 2, 3)
        self.assertEqual(self.solver_obj, obj)

    def test_to_set_interval(self):
        obj = ode_solver.OdeSolver(1, 2, 3)
        obj.set_time_interval(10)
        self.assertEqual(obj.get_time_interval(), 10)

    def test_to_get_time_interval(self):
        obj = ode_solver.OdeSolver(1, 2, 3)
        self.assertEqual(obj.get_time_interval(), 0.02)

    def test_to_set_num_of_steps(self):
        obj = ode_solver.OdeSolver(1, 2, 3)
        obj.set_num_of_steps(10)
        self.assertEqual(obj.get_num_of_steps(), 10)

    def test_to_get_num_of_steps(self):
        obj = ode_solver.OdeSolver(1, 2, 3)
        self.assertEqual(obj.get_num_of_steps(), 10000)

    def test_simulator(self):
        obj = ode_solver.OdeSolver(10, 2.5, 16)
        obj.set_num_of_steps(2)
        print("Simulation")
        result = obj.simulator(1, 1, 1)
        xyz_dict = dict()
        xyz_dict['x_val'] = [1, 1.0]
        xyz_dict['y_val'] = [1, 1.28]
        xyz_dict['z_val'] = [1, 0.97]
        print(result)

        self.assertEqual(result, xyz_dict)


if __name__ == '__main__':
    unittest.main()
