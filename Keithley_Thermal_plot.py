import matplotlib.pyplot as plt
from matplotlib import interactive
import numpy as np

# calculate normalized resistance


def norm(arr):  # Define a function dividing R values by the initial R value
    arr_res = arr[:,2]
    init_res = arr_res[0]
    for i in range(len(arr_res)):
        arr_res[i] = arr_res[i]/init_res
    return arr_res


def minute(arr):  # Define a function that converts time in seconds to mins
    arr_t = arr[:,0]
    for i in range(len(arr_t)):
        arr_t[i] = arr_t[i]/60
    return arr_t


data_path1_T = 'C:\\Users\\CHAE\\Dropbox (MIT)\\Research\\Keithley data\\Thermal\\190401_annealed_AgNW50_1to8_600rpmonce_Tramp_T.txt'
data_path1_R = 'C:\\Users\\CHAE\\Dropbox (MIT)\\Research\\Keithley data\\Thermal\\190401_annealed_AgNW50_1to8_600rpmonce_Tramp_R.txt'
data_path2_T = 'C:\\Users\\CHAE\\Dropbox (MIT)\\Research\\Keithley data\\Thermal\\190404_EPDGO_Tramp_T.txt'
data_path2_R = 'C:\\Users\\CHAE\\Dropbox (MIT)\\Research\\Keithley data\\Thermal\\190404_EPDGO_Tramp_R_1.txt'
data_path3_T = 'C:\\Users\\CHAE\\Dropbox (MIT)\\Research\\Keithley data\\Thermal\\190401_EPDGO_AgNW_0322_1_Tramp_T.txt'
data_path3_R = 'C:\\Users\\CHAE\\Dropbox (MIT)\\Research\\Keithley data\\Thermal\\190401_EPDGO_AgNW_0322_1_Tramp_R.txt'

data1_T = np.genfromtxt(data_path1_T, delimiter=',')
data1_R = np.genfromtxt(data_path1_R, delimiter=',')
data2_T = np.genfromtxt(data_path2_T, delimiter=',')
data2_R = np.genfromtxt(data_path2_R, delimiter='\t')
data3_T = np.genfromtxt(data_path3_T, delimiter=',')
data3_R = np.genfromtxt(data_path3_R, delimiter=',')

# font dictionary
font = {'family': 'Arial',
        'weight': 'normal',
        'size': 16,
        }

fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111)
line, = ax1.plot(minute(data1_T), data1_T[:, 1], 'b')  # Plotting time vs. Temperature
plt.plot(minute(data2_T), data2_T[:, 1], 'k')
plt.plot(minute(data3_T), data3_T[:, 1], 'r')
plt.xlabel('Time (min)', fontdict=font)
plt.ylabel('Temperature ($^\circ$C)', fontdict=font)
plt.xticks(fontname='arial', fontsize=15)
plt.yticks(fontname='arial', fontsize=15)
ax1.yaxis.set_major_locator(plt.MaxNLocator(6)) # set number of y axis ticks
ax1.xaxis.set_major_locator(plt.MaxNLocator(5)) # set number of x axis ticks
# plt.grid(True)    # show grids
plt.xlim(0, 200)
plt.ylim(0, 350)

leg = plt.legend(['AgNW only','EPD-GO only','EPD-GO/AgNW'], prop=font)
leg.get_frame().set_edgecolor('k')  # set legend box color

interactive(True)
plt.show()

fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111)
line, = ax2.plot(data1_T[:, 1], data1_R[:, 1], 'b')  # Plotting Temperature vs. Resistance
plt.plot(data2_T[:, 1], data2_R[:, 1], 'k')
plt.plot(data3_T[:, 1], data3_R[:, 1], 'r')
plt.xlabel('Temperature ($^\circ$C)', fontdict=font)
plt.ylabel('Resistance ($\Omega$)', fontdict=font)
plt.xticks(fontname='arial', fontsize=15)
plt.yticks(fontname='arial', fontsize=15)
ax2.yaxis.set_major_locator(plt.MaxNLocator(6)) # set number of y axis ticks
ax2.xaxis.set_major_locator(plt.MaxNLocator(6)) # set number of x axis ticks
plt.xlim(180, 350)
plt.ylim(30, 10000)
plt.yscale('log')   # y axis log scale

leg = plt.legend(['AgNW only', 'EPD-GO only','EPD-GO/AgNW'], loc='upper left', prop=font)
leg.get_frame().set_edgecolor('k')  # set legend box color

interactive(False)
plt.show()