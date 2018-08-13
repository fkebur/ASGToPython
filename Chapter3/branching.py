# -*- coding: utf-8 -*-
# Python 3.6
# branching.py

"""
Author: Kebur Fantahun
Created: Sun Aug 12 08:14:27 2018
Modified: Sun Aug 12 08:14:27 2018

Description: this script illustrates branching
-----------
"""

import numpy as np, matplotlib.pyplot as plt

for trial in range(5):
    userInput = input('Pick a number: ')
    number = float(userInput)
    if number < 0:
        print('Square root is not real')
    else:
        print('Square root of {} is {:.7f}.'.format(number, np.sqrt(number)))
    userAgain = input('Another [y/n]?')
    if userAgain != 'y':
        break

#%% Check whether the loop terminated normally
if trial == 4:
    print('Sorry, only 5 per customer.')
elif userAgain == 'n':
    print('Bye!')
else:
    print('Sorry, I did not understand that')
