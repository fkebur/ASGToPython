# -*- coding: utf-8 -*-
# Python 3.6

"""
Author: Kebur Fantahun

Created: Sun Aug 26 10:23:50 2018
Modified: Sun Aug 26 10:23:50 2018

Description: function example; YourTurn6A
"""
import numpy as np, matplotlib.pyplot as plt

# excerpt from measurements.py
def taxicab(pointA, pointB):
    """
    Taxicab metric for computing the distance between points A and B.
        pointA = (x1,y1)
        pointB = (x2,y2)
    Returns |x2-x1| + |y2-y1|. Distances are measured in city blocks.
    """
    interval = abs(pointB[0] - pointA[0]) + abs(pointB[1] - pointA[1])
    return interval
def taxicab3D(pointC, pointD):
    """
    Taxicab metric for computing the distance between points A and B.
        pointC = (x1,y1,z1)
        pointD = (x2,y2,z2)
    Returns |x2-x1| + |y2-y1| + |z2-z1|. Distances are measured in city blocks.
    """
    interval = abs(pointD[0] - pointC[0]) + abs(pointD[1] - pointC[1]) + \
    abs(pointD[2] - pointC[2])
    return interval

def taxi(point):
    i = abs(point)
    return i

'''
from imp import reload
reload(measurements)

this allows one to update functions in an already imported module
'''