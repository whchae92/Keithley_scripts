# -*- coding: utf-8 -*-
# Import necessary packages
from pymeasure.instruments.keithley import Keithley2400
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import sleep

# Set the input parameters
data_points = 50
averages = 50
max_voltage = 1
min_voltage = -max_voltage

# Connect and configure the instrument
sourcemeter = Keithley2400("ASRL3::INSTR")  #using RS 232 COM3
sourcemeter.reset()
sourcemeter.use_front_terminals()
sourcemeter.measure_current()
sourcemeter.apply_voltage()
sourcemeter.source_voltage = min_voltage  # Sets the source current to min current mA
sourcemeter.enable_source()
sleep(0.1) # wait here to give the instrument time to react

# Allocate arrays to store the measurement results
voltages = np.linspace(min_voltage, max_voltage, num=data_points)
currents = np.zeros_like(voltages)
currents_stds = np.zeros_like(voltages)
sleep(0.1)

# Loop through each current point, measure and record the voltage
for i in range(data_points):
    sourcemeter.start_buffer()
    sourcemeter.source_voltage = voltages[i]
    sleep(0.1)
    # Record the average voltage and standard deviation
    currents[i] = sourcemeter.current
    currents_stds[i] = sourcemeter.std_current

# Save the data columns in a CSV file
data = pd.DataFrame({
    'Voltage (V)': voltages,
    'Current (A)': currents,
    'Current Std (A)': currents_stds,
})
data.to_csv('example.csv')

# Plot the data with the standard deviation as error bar, note in this example yerr=0.01 to be visible take your voltage_stds in your experiments
plt.errorbar(voltages, currents, yerr=0.01, fmt='.k')
plt.ylabel('Current (A)')
plt.xlabel('Voltage (V)')
plt.title('I-V plot')

sourcemeter.shutdown()