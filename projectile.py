# -*- coding: utf-8 -*-
# projectile.py
# Python 3.6

"""
Author: Kebur Fantahun
Created: Sat Aug 11 01:42:20 2018
Modified: Sat Aug 11 01:42:20 2018

Description: copy of Kinders code from python book
==================================================

Calculate how long an object is in the air when thrown from a specificied
height with a range of initial speeds assuming constant acceleration due to
gravity:
    0.5 * g * t**2 - vO * t - yO = 0
   
"""

import numpy as np

#%% Initialize variable.
initial_speed = 1.0         # vO = initial vertical speed of ball [m/s]
impact_time = 0.0           # t = time of impact [s] (computed in loop)

#%% Initialize parameters.
g = 9.8066                  # Gravitational acceleration [m/s^2]
initial_height = 10.0        # yO = height ball is thrown from [m]
speed_increment = 5.0       # Speed increment for each iteration [m/s]
cutoff_time = 10.0          # Stop computing after impact time exceeds cutoff

#%% Calculate and display impact time. Increment initial speed each step.
#   Repeat until impact time exceeds cutoff
while impact_time < cutoff_time:
    # use quadratic equation to solve kinematic equation for impact time:
    impact_time = (np.sqrt(initial_speed**2 + 2 * g * initial_height ) \
                   +  initial_speed) / g
    print("speed= {} m/s; time = {:.1f} s".format(initial_speed, impact_time))
    initial_speed += speed_increment
print("Calculation complete.")

