# -*- coding: utf-8 -*-
# Python 3.6

"""
Author: Kebur Fantahun

Created: Tue Aug 14 03:05:34 2018
Modified: Tue Aug 14 03:05:34 2018

Description: replace curves
"""
import numpy as np, matplotlib.pyplot as plt

x = np.arange(0, 20, .2)

plt.plot(x, 3*x)             # Plot two lines.
plt.plot(x, x**3)
plt.xlabel('Time[s]')        #Label axes.
plt.ylabel('Position[cm]')

plt.ylim(0,450)              # Zoom into curves

ax = plt.gca()               # Assign a name to the current Axes object.
lines = ax.get_lines()       # Assign a name to its list of Line onjects.
lines[1].set_data(x,x**2)    # Replace plot data of second line

plt.figure()
plt.show()