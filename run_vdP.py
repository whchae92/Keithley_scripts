# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:57:04 2020

@author: wchae
"""

# Outputs sheet resistance value from four sweeps performed using Keithley_4_wire_resistance.py

import math as m
import pandas as pd
from scipy.optimize import fsolve
import numpy as np

path1 = 'C:/Users/whcha/Dropbox (MIT)/Research/Data/Keithley data/vdp/201203_JP_PEDOT_sio2/1k_1.csv'
path2 = 'C:/Users/whcha/Dropbox (MIT)/Research/Data/Keithley data/vdp/201203_JP_PEDOT_sio2/1k_2.csv'
path3 = 'C:/Users/whcha/Dropbox (MIT)/Research/Data/Keithley data/vdp/201203_JP_PEDOT_sio2/1k_3.csv'
path4 = 'C:/Users/whcha/Dropbox (MIT)/Research/Data/Keithley data/vdp/201203_JP_PEDOT_sio2/1k_4.csv'

def slope(data_path):
    df = pd.read_csv(data_path)
    slope = np.polyfit(df['Current (A)'], df['Voltage (V)'], 1)[0]
    return slope
    
Rv = (slope(path1) + slope(path2))/2   # Vertical resistance
Rh = (slope(path3) + slope(path4))/2   # Horizontal resistance

def func(x):  # Defining vdP equation
    return m.exp(-m.pi*Rv/x) + m.exp(-m.pi*Rh/x) - 1

Rs = fsolve(func, 1) 
    
    