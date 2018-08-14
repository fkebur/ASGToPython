# -*- coding: utf-8 -*-
# Python 3.6

"""
Author: Kebur Fantahun

Created: Tue Aug 14 02:17:26 2018
Modified: Tue Aug 14 02:17:26 2018

Description: YourTurn4A from book
"""
import numpy as np, matplotlib.pyplot as plt

num_points = 5
nom_points = 5
x_min, x_max = 0, 4
x_values = np.linspace(x_min, x_max, num_points)
y_values = x_values**2
x_values = np.linspace(x_min, x_max, nom_points)

assert len(x_values) == len(y_values), \
    "Length-mismatch: {:d}".format(len(x_values),len(y_values))

plt.plot(x_values, y_values, label="E=mc^2")

# Make the line smooth, red and thick
ax = plt.gca()
lines = ax.get_lines()
plt.setp(lines[0], linestyle='-', linewidth=5, color='r')

# Add axes labels
ax.set_xlabel("Speed of light")
ax.set_ylabel("Mass energy")

# Add title
ax.set_title("Einstein mass-energy relation")

# Add legend
plt.legend(loc=2, prop={'size': 26})