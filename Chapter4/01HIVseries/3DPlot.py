# -*- coding: utf-8 -*-
# Python 3.6
# line3d,py
"""
Author: Kebur Fantahun

Created: Tue Aug 14 16:45:02 2018
Modified: Tue Aug 14 16:45:02 2018

Description: 3d graph
"""
import numpy as np, matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D # Get 3D plotting tool.

fig = plt.figure()      # Create a new figure.
ax = Axes3D(fig)        # Create 3D plotter attached to figure.
t = np.linspace(0, 5*np.pi, 501)    # Define parameter for parametric plot.
ax.plot(np.cos(t), np.sin(t), t)    # Draw 3D plot.

ax.view_init(elev=30,azim=30)       # if backend is set, one may click/drag
                                    # the plot