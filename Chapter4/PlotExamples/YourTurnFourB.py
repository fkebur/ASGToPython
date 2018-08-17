# -*- coding: utf-8 -*-
# Python 3.6
# YourTurnFourB.py
"""
Author: Kebur Fantahun

Created: Tue Aug 14 22:12:40 2018
Modified: Tue Aug 14 22:12:40 2018

Description: 4B from the book
"""
import numpy as np, matplotlib.pyplot as plt

num_curves = 3

x = np.linspace(0, 1, 51)
y = np.zeros((x.size,num_curves))

for n in range(num_curves):
    y[:,n] = np.sin((n+1) * x * 2 * np.pi)
plt.plot(x,y)

# open and close any extra figures with the below code
plt.figure('Jack')
plt.close('Jack')

# legend embellishment
ax = plt.gca()
ax.legend((r"$\sin(2 \pi x)$",r"$\sin(4 \pi x)$",r"$\sin(6 \pi x)$"))
