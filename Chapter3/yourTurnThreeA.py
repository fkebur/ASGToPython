# -*- coding: utf-8 -*-
# yourTurnThreeA.py
# Python 3.6

"""
Author: Kebur Fantahun
Created: Fri Aug 10 00:02:07 2018
Modified: Fri Aug 10 00:02:07 2018

Description: Your Turn 3A ; ASGTPython
-----------
"""

import numpy as np
from scipy.special import factorial

# part A
def gauss(x):
    return np.exp(-x**2)
x = np.arange(-1, 2, 0.2)

# part B
def facts(mu, n):
    return (np.exp(-mu)*mu**n)/factorial(n)
