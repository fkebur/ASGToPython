# -*- coding: utf-8 -*-
# Python 3.6

"""
Author: Kebur Fantahun

Created: Tue Aug 14 10:07:21 2018
Modified: Tue Aug 14 10:07:21 2018

Description:
"""
import numpy as np, matplotlib.pyplot as plt

num_points = 5
x_min, x_max = 0, 4
x_values = np.linspace(x_min, x_max, num_points)
y_values = x_values**2
x_errors = [0,.2,.5,1.2,.2]
y_errors = [1,.6,.1,1.6,.4]
plt.errorbar(x_values, y_values, yerr=y_errors, xerr=x_errors)

ax = plt.gca()
ax.set_title("First errorbars", size=24, weight='bold')