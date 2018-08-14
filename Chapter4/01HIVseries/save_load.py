# -*- coding: utf-8 -*-
# Python 3.6

"""
Author: Kebur Fantahun

Created on Mon Aug 13 20:21:54 2018
Modified on Mon Aug 13 22:25:54 2018

Description: save_load.py
"""
import numpy as np

#, matplotlib.pyplot as plt

x = np.linspace(0, 1, 1001)
y = 3*np.sin(x)**3 - np.sin(x)

np.save('x_values', x)
np.save('y_values', y)
np.savetxt('x_values.dat', x)
np.savetxt('y_values.dat', y)
np.savez('xy_values',x_vals=x,y_vals=y)