# -*- coding: utf-8 -*-
# Python 3.6
# ExpFit.py
"""
Author: Kebur Fantahun

Created: Wed Aug 15 18:17:49 2018
Modified: Wed Aug 15 18:17:49 2018

Description: Fit experimental data; Lab1
"""
import numpy as np, matplotlib.pyplot as plt

# Fill variable with single array of all values in csv file
# hiv_data = np.loadtxt("HIVSeries.csv", delimiter=",")

# Same as the comment above but for non-(csv,txt,...,etc.) formats
# hiv_data = np.load("HIVSeries.npy")

# Fill variable with non human readable numpy.lib file
hiv_data = np.load("HIVSeries.npz")

# HIV data split into respective numpy arrays
treatment_time = hiv_data['time_in_days']
concentration = hiv_data['viral_load']

# Data model

# paramters
alpha = 3.62e-1 # might be the correct alpha, roughly -- 0.09974999999999999
beta  = 6e-1
A = 6.605e4 
B = 1.002e5 

# time array and viral load prediction formula
time = np.linspace(0, 10, 101)
viral_load = A * np.exp(-alpha*time) + B * np.exp(-beta*time)

# plot data
plt.plot(treatment_time, concentration, 'r*', time, viral_load, 'bx')

# Embellish plot
ax = plt.gca()
ax.set_title("Antiretroviral HIV treatment", size=24, weight='bold')
ax.set_xlabel('Time[Days]')
ax.set_ylabel('Virus concentration [per mL]')