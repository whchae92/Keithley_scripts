# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 11:06:23 2020

@author: wchae
"""

# Initiates 4-wire sensing mode and performs IV sweep for van der Pauw measurement
# Displays I-V plot and saves data as csv file

from pymeasure.instruments.keithley import Keithley2400
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import sleep

# Set the input parameters
data_points = 50
averages = 50
max_current = 0.01
min_current = -max_current

# Connect and configure the instrument
sourcemeter = Keithley2400("ASRL3::INSTR")  #using RS 232 COM3
sourcemeter.reset()
sourcemeter.use_front_terminals()
sourcemeter.wires = 4 # using 4 wire sense mode
sourcemeter.measure_voltage()
sourcemeter.apply_current(compliance_voltage=50)
sourcemeter.source_current = min_current  # Sets the source current to min current mA
sourcemeter.enable_source()
sleep(0.1) # wait here to give the instrument time to react

# Allocate arrays to store the measurement results
currents = np.linspace(min_current, max_current, num=data_points)
voltages = np.zeros_like(currents)
voltages_stds = np.zeros_like(currents)
sleep(0.1)

# Loop through each current point, measure and record the voltage
for i in range(data_points):
    sourcemeter.start_buffer()
    sourcemeter.source_current = currents[i]
    sleep(0.1)
    # Record the average voltage and standard deviation
    voltages[i] = sourcemeter.voltage
    voltages_stds[i] = sourcemeter.std_voltage

# Save the data columns in a CSV file
data = pd.DataFrame({
    'Current (A)': currents,
    'Voltage (V)': voltages,
    'Voltage Std (V)': voltages_stds,
})
data.to_csv('C://Users/whcha//Dropbox (MIT)//Research//Data//Keithley data//vdP//201203_JP_PEDOT_sio2//4k_4.csv', line_terminator='\r')

# Plot the data with the standard deviation as error bar, note in this example yerr=0.01 to be visible take your voltage_stds in your experiments
plt.plot(currents, voltages)
plt.ylabel('Voltage (V)')
plt.xlabel('Current (A)')
plt.title('I-V plot')

sourcemeter.shutdown()