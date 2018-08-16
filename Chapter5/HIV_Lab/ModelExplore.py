# -*- coding: utf-8 -*-
# Python 3.6
# ModelExplore.py
"""
Author: Kebur Fantahun

Created: Wed Aug 15 00:09:04 2018
Modified: Wed Aug 15 00:09:04 2018

Description: First computer lab; HIV Example
"""
import numpy as np, matplotlib.pyplot as plt
 
# paramters
alpha = 1e-1
beta  = 1e0
A = 1.75e5
B = 10

# time array and viral load prediction formula
time = np.linspace(0, 10, 101)
viral_load = A * np.exp(-alpha*time) + B * np.exp(-beta*time)

# plot
plt.plot(time,viral_load)
