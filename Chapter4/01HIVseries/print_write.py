# -*- coding: utf-8 -*-
# Python 3.6
# print_write.py
"""
Author: Kebur Fantahun

Created on Mon Aug 13 22:24:37 2018
Modified on Mon Aug 13 22:24:37 2018

Description: file write script
"""
import numpy as np, matplotlib.pyplot as plt

my_file = open('power.txt','w')
print( " N \t\t2**N\t\t3**N" )      # Print labels for columns.
print( "---\t\t----\t\t----" )      # Print seperator.
my_file.write( " N \t\t2**N\t\t3**N" )      # Write labels to columns.
my_file.write( "---\t\t----\t\t----" )      # Write seperator to file.
#%% Loop over integers from 0 to 10 and print/write results.
for N in range(11):
    print( "{:d}\t\t{:d}\t\t{:d}".format(N, pow(2, N), pow(3, N)) )
    my_file.write( "{:d}\t\t{:d}\t\t{:d}".format(N, pow(2, N), pow(3, N)) )
my_file.close()