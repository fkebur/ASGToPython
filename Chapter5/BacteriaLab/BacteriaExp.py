# -*- coding: utf-8 -*-
# Python 3.6
# BacteriaExp.py
"""
Author: Kebur Fantahun

Created: Thu Aug 16 10:10:24 2018
Modified: Thu Aug 16 10:10:24 2018

Description: Bacterial example
"""
import numpy as np, matplotlib.pyplot as plt

# Same as the comment above but for non-(csv,txt,...,etc.) formats
bacteria_data_high = np.load("g149novickA.npy")
bacteria_data_low = np.load("g149novickB.npy")

# equations
def VPop(t, tau):
    return 1 - np.exp(-t/tau)
def WPop(t, A, tau):
    return A * (np.exp(-t/tau) -1 + (t/tau))

# setup arrays for olotting
t = np.arange(0,7,3e-3)
timeH=[]
timeL= []
proteinActH=[]
proteinActL = []

# fill high inducer data arrays
for i in range(len(bacteria_data_high)):
    proteinActH.append(bacteria_data_high[i][1])
    timeH.append(bacteria_data_high[i][0])

# fill low inducer data arrays
for j in range(len(bacteria_data_low)):
    proteinActL.append(bacteria_data_low[j][1])
    timeL.append(bacteria_data_low[j][0])

# clear plot for re running program
plt.gcf().clear()

# Experimental Model with V(t) plot
# plt.plot(t, 1e1*VPop(t, 5e1), 'r--', label=r'$\tau =  5e1$')
# plt.plot(t, 4e2*VPop(t, 1e5), 'c-' , label=r'$\tau =  1e5$')
# plt.plot(t, 1e1*VPop(t, 1e10), 'b-.', label=r'$\tau = 90$')
# plt.plot(t, 1e1*VPop(t, 1e15), 'm:', label=r'$\tau = 180$')

# Experimental Model with W(t) plot
# plt.plot(t, WPop(t, 1e3, 1e3), 'bo', label=r'$A = 1  ,\tau = 1e2$')
plt.semilogy(t, WPop(t, 0.36, 1), 'r--')#  label=r'$A = 1  ,\tau = 5e1$')
# plt.plot(WPop(t, 6e2, 0.5) + 2.4, t,  'c-' , label=r'$A = 1  ,\tau = 1e5$')

# How can I improve these curves? ...

# limits
plt.xlim(0.1,10)

# Data plot; high inducer
plt.semilogy(timeH, proteinActH, 'yx', label='High inducer')

# Data plot; low inducer
# plt.plot(timeL, proteinActL, 'k+', label='Low inducer')

plt.legend()

ax = plt.gca()
ax.set_title("Bacterial culture production", size=16, weight='bold')

ax.set_xlabel('Time(hours)')
ax.set_ylabel('Fraction of maximum beta-galactosidase activity')

"""
Experimental model with W(t)
plt.plot(t, WPop(t, 1 , 1), 'r--', label=r'$A = 1  ,\tau = 1$')
plt.plot(t, WPop(t, 1, -1), 'c-', label=r'$A = 1  , \tau = -1$')
plt.plot(t, WPop(t, -1, 1), 'b-.',label=r'$A = -1,\tau = 1$')
plt.plot(t, WPop(t, -1, -1), 'r:',label=r'$A = -1,\tau = -1$')

...

Method with arrays:

W1 = [1, 1]
W2 = [1, -1]
W3 = [-1, 1]
W4 = [-1, -1]

plt.plot(t, WPop(t, W1[0] , W1[1]),'r--', t, WPop(t, W2[0] , W2[1]), 'c-',\
         t, WPop(t, W3[0] , W3[1]),'b-.', t, WPop(t, W4[0] , W4[1]), 'r:' )

"""