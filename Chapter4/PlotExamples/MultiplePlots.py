# -*- coding: utf-8 -*-
# Python 3.6
# MultiplePlots.py
"""
Author: Kebur Fantahun

Created: Tue Aug 14 16:59:31 2018
Modified: Tue Aug 14 16:59:31 2018

Description: plot two lines with customization(embellishment)
"""
import numpy as np, matplotlib.pyplot as plt

x = np.linspace(0,1,51)
y1 = np.exp(x)
y2 = x**2
plt.plot(x, y1,'r', x, y2, 'kx')

