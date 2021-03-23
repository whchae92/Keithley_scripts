# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 11:27:24 2020

@author: whcha
"""

# Input: four IV sweep results csv files as dataframe
# Calculate resistance from the four sweeps by linear regression and slope determination
# Calculate vertical (Rv) and horizontal (Rh) average resistance of the film
# Solve the vdP equation with Rv and Rh
# Output Rs