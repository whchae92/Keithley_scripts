import matplotlib.pyplot as plt
from matplotlib import interactive
import numpy as np

# calculate normalized resistance


def norm(arr):  # Define a function dividing R values by the initial R value
    arr_res = arr[:,1]
    init_res = arr_res[0]
    for i in range(len(arr_res)):
        arr_res[i] = arr_res[i]/init_res
    return arr_res

def norm_mech(arr):  # Define a function dividing R-R0 values by the initial R value
    arr_res = arr[:,1]
    init_res = arr_res[0]
    for i in range(len(arr_res)):
        arr_res[i] = (arr_res[i]-init_res)/init_res
    return arr_res

def mins(arr):  # Define a function that converts time in seconds to mins
    arr_t = arr[:,0]
    for i in range(len(arr_t)):
        arr_t[i] = arr_t[i]/60
    return arr_t

def hrs(arr):  # Define a function that converts time in seconds to hrs
    arr_t = arr[:,0]
    for i in range(len(arr_t)):
        arr_t[i] = arr_t[i]/3600
    return arr_t

def cycles(arr):  # Define a function that converts time in seconds to no of cycles
    arr_t = arr[:,0]
    for i in range(len(arr_t)):
        arr_t[i] = arr_t[i]/17 #choose length of a single cycle in seconds
    return arr_t


data_path1 = 'C:\\Users\\CHAE\\Dropbox (MIT)\\Research\\Keithley data\\mechanical\\042419\\042419_bareAgNW50_PEN_2_pretest_syringe_3ml_5000cycles.txt'
# data_path2 = 'C:\\Users\\CHAE\\Dropbox (MIT)\\Research\\Keithley data\\mechanical\\042119\\041819_EPDGO_AgNW50_PET_3hrs_1_syringe_4ml.txt'
# data_path1 = "/Users/chae/Dropbox (MIT)/Research/Keithley data/mechanical/042419/042419_bareAgNW50_PEN_1_syringe_3ml_6hrs.txt"
# data_path2 = "/Users/chae/Dropbox (MIT)/Research/UV-vis spectra/181001/1001_700rpm_diffT_PLL_bare.csv"

data1 = np.genfromtxt(data_path1, delimiter='\t')
# data2 = np.genfromtxt(data_path2, delimiter='\t')

# font dictionary
font = {'family': 'Arial',
        'weight': 'normal',
        'size': 16,
        }

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
line, = ax1.plot(cycles(data1), norm_mech(data1), 'k')  # Plotting Time vs. Resistance
# plt.plot(cycles(data2), norm(data2), 'b')
plt.xlabel('Bending cycle number', fontdict=font)
plt.ylabel('$(R-R_0)/R_0$', fontdict=font)
plt.xticks(fontname='arial', fontsize=15)
plt.yticks(fontname='arial', fontsize=15)
ax1.yaxis.set_major_locator(plt.MaxNLocator(6)) # set number of y axis ticks
ax1.xaxis.set_major_locator(plt.MaxNLocator(5)) # set number of x axis ticks
# plt.yscale('log')   # y axis log scale
# plt.grid(True)    # show grids
plt.xlim(0, 80)
plt.ylim(-0.02, 0.06)

leg = plt.legend(['bare AgNW', 'EPD-GO/AgNW'], prop=font)
leg.get_frame().set_edgecolor('k')  # set legend box color

plt.show()