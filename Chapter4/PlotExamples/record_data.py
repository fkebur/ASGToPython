# -*- coding: utf-8 -*-
# Python 3.6

"""
Author: Kebur Fantahun

Created on Mon Aug 13 21:53:41 2018
Modified on Mon Aug 13 22:25:54 2018

Description: recover data from save_load
"""
import numpy as np, matplotlib.pyplot as plt

x2 = np.load('x_values.npy')
y2 = np.loadtxt('y_values.dat')
w = np.load('xy_values.npz')
