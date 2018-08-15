# -*- coding: utf-8 -*-
# Python 3.6
# subplots.py
"""
Author: Kebur Fantahun

Created: Tue Aug 14 23:38:38 2018
Modified: Tue Aug 14 23:38:38 2018

Description: subplot example
"""
import numpy as np, matplotlib.pyplot as plt
from numpy.random import random

t = np.linspace(0, 1, 100)
plt.figure()
plt.subplot(2, 2, 1); plt.hist(random(20))                      # Upper left
plt.subplot(2, 2, 2); plt.plot(t, t**2, t, t**3 - t)            # Upper right
plt.subplot(2, 2, 3); plt.plot(random(20), random(20), 'r*')    # Lower left
plt.subplot(2, 2, 4); plt.plot(t*np.cos(10*t), t*np.sin(10*t))  # Lower right

# To resize the figure window when figures overlap or do not fit nicely
# plt.tight_layout
# 
# For more info see plt.axes

fig = plt.gcf()     # Get current figure object.
fig.canvas.get_supported_filetypes()
plt.savefig('greatest_figure_ever.pdf')

'''
See 4.3.9 in the python book for vector-graphics applications, etc.

Before saving the fig, use the following to change how fonts are saved for .svg files
import natplotlib
matplotlib.rcParams['svg.fonttype'] = 'none'
Then save the file as an svg
 
For editing pdfs(and maybe other filetypes?)
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42

For publishing -- vector is best
For a presentation -- bitmap is best (i.e. .gif, .png, .jpg, or .tif)
'''