# -*- coding: utf-8 -*-
# Python 3.6
# simple_plot.py
"""
Author: Kebur Fantahun

Created: Mon Aug 13 22:44:20 2018
Modified: Mon Aug 13 22:44:20 2018

Description: simple... but detailed plot script
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

plt.plot(x_values, y_values)
plt.xlim(1,6),plt.ylim(1,10)

ax = plt.gca()
ax.set_title("My first plot", size=24, weight='bold')
# or plt.title("My first plot", size=24, weight='bold')

ax.set_xlabel('Speed')
ax.set_ylabel('Kinetic energy')
# or plt instead of ax

ax.set_xticklabels(ax.get_xticks(), family = "monospace", fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family = "monospace", fontsize=10)

lines = ax.get_lines()
# Lines is a list of line objects.
# Make the first line thick, dashed, and red.
plt.setp(lines[0], linestyle='--', linewidth=3, color='r')

# Use label keyword to set labels when plotting.
plt.plot(x_values, y_values, label="Population 1")
plt.plot(x_values, x_values**3, label="Population 2")
plt.legend()
# Display legend in plot

# Use line objects to set labels after plotting
ax = plt.gca()
lines = ax.get_lines()
lines[0].set_label("Infected Population")
lines[1].set_label("Cured Population")
ax.legend()
# Display legend in plot

ax.legend(("Healthy","Recovered"))
