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


data_path1 = 'C:\\Users\\CHAE\\Dropbox (MIT)\\Research\\Keithley data\\Electrical\\190405_2_bare_AgNW50_vramp_newcontact_IRcam.txt'
# data_path2 = 'C:\\Users\\CHAE\\Dropbox (MIT)\\Research\\Keithley data\\112018_noPLLGONW_vramptest.txt'
data_path3 = 'C:\\Users\\CHAE\\Dropbox (MIT)\\Research\\Keithley data\\Electrical\\190322_2_EPDGO_AgNW_vramp_newcontact_IRcam.txt'
# data_path3 = 'C:\\Users\\CHAE\\Dropbox (MIT)\\Research\\Keithley data\\110718_PLLGONW_vramptest.txt'
# data_path4 = 'C:\\Users\\CHAE\\Dropbox (MIT)\\Research\\Keithley data\\181205_EPDGO_AgNW_vramp.txt'

data1 = np.genfromtxt(data_path1, delimiter=',')
# data2 = np.genfromtxt(data_path2, delimiter=',')
data3 = np.genfromtxt(data_path3, delimiter=',')
# data4 = np.genfromtxt(data_path4, delimiter=',')

# font dictionary
font = {'family': 'Arial',
        'weight': 'normal',
        'size': 16,
        }

fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111)
# ax2 = ax1.twinx() # second y axis that shares x axis
ax1.plot(data1[:, 1], data1[:, 2], 'k')  # Plotting Voltage vs. Resistance
# ax2.plot(data1[:, 1], )
# plt.plot(data2[:, 1], data2[:, 2], 'r')
plt.plot(data3[:, 1], data3[:, 2], 'b')
# plt.plot(data4[:, 1], data4[:, 2], 'g')
plt.xlabel('Voltage (V)', fontdict=font)
plt.ylabel('Resistance ($\Omega$)', fontdict=font)
plt.xticks(fontname='arial', fontsize=15)
plt.yticks(fontname='arial', fontsize=15)
ax1.yaxis.set_major_locator(plt.MaxNLocator(6)) # set number of y axis ticks
ax1.xaxis.set_major_locator(plt.MaxNLocator(5)) # set number of x axis ticks
# plt.yscale('log')   # y axis log scale
# plt.grid(True)    # show grids
plt.xlim(0, 20)
plt.ylim(0, 1000)

plt.style.use('classic')
leg = plt.legend(['Bare AgNW', 'EPD GO/AgNW'], loc='upper left', prop=font)
leg.get_frame().set_edgecolor('k')  # set legend box color

interactive(True)
plt.show()

plt.style.use('default')

fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111)
ax2.plot(data1[:, 1], norm(data1), 'k')  # Plotting Voltage vs. Normalized Resistance
# plt.plot(data2[:, 1], norm(data2), 'r')
plt.plot(data3[:, 1], norm(data3), 'b')
# plt.plot(data4[:, 1], norm(data4), 'g')
plt.xlabel('Voltage (V)', fontdict=font)
plt.ylabel('Normalized Resistance', fontdict=font)
plt.xticks(fontname='arial', fontsize=15)
plt.yticks(fontname='arial', fontsize=15)
ax2.yaxis.set_major_locator(plt.MaxNLocator(6)) # set number of y axis ticks
ax2.xaxis.set_major_locator(plt.MaxNLocator(5)) # set number of x axis ticks
plt.xlim(0, 20)
plt.ylim(0, 50)

plt.style.use('classic')
leg = plt.legend(['Bare AgNW', 'EPD GO/AgNW'], loc='upper left', prop=font)
leg.get_frame().set_edgecolor('k')  # set legend box color

interactive(False)
plt.show()
