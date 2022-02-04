import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import pandas as pd
import spinmob as sm
import mcphysics as mphys
from scipy.optimize import curve_fit

#Gaussian, where m=peak, o=variance, A=amplitude, B=Linear Coeff., C=Linear Offset
def Gaussian(x, m, o, A, B, C):
    return A*np.exp(-0.5*(((x-m)/o)**2)) + B*x + C

#Curve fits a Gaussian to a given emitter's callibration data curve. The interval determines the width of data
#which the Gaussian fits around. 
def Fit(input_databox, interval, guess):
    xData = np.arange(0, 2048)
    param, cov = curve_fit(Gaussian, xData[guess-interval:guess+interval], 
                           input_databox[guess-interval:guess+interval], p0=[guess, 10, 10, 10, 10])
    error = np.sqrt(np.diag(cov))
    print(param), print(error)
    return [param, error]

### Al 55
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Aluminum/02 Aluminum 55 degrees 000.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Aluminum/02 Aluminum 55 degrees 024.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 55 - Aluminum')
plt.show()

Al_55param = Fit(data, 200, 607)

### Al 75
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Aluminum/02 Aluminum 75 degrees 024.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Aluminum/02 Aluminum 75 degrees 030.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 75 - Aluminum')
plt.show()

Al_75param = Fit(data, 200, 692)

### Al 95
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Aluminum/02 Aluminum 95 degrees 002.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Aluminum/02 Aluminum 95 degrees 028.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 95 - Aluminum')
plt.show()

Al_95param = Fit(data, 200, 835)

### Al 125
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Aluminum/02 Aluminum 125 degrees 027.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Aluminum/02 Aluminum 125 degrees 036.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 125 - Aluminum')
plt.show()

Al_125param = Fit(data, 200, 1125)

### Al 220
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Aluminum/02 Aluminum 220 degrees 036.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Aluminum/02 Aluminum 220 degrees 039.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 220 - Aluminum')
plt.show()

Al_220param = Fit(data, 200, 1370)

### Al 240
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Aluminum/02 Aluminum 240 degrees 002.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Aluminum/02 Aluminum 240 degrees 007.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 240 - Aluminum')
plt.show()

Al_240param = Fit(data, 200, 1103)

### Al 260
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Aluminum/02 Aluminum 260 degrees 006.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Aluminum/02 Aluminum 260 degrees 039.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 260 - Aluminum')
plt.show()

Al_260param = Fit(data, 200, 879)

### Al 300
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Aluminum/02 Aluminum 300 degrees 017.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Aluminum/02 Aluminum 300 degrees 032.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 300 - Aluminum')
plt.show()

Al_300param = Fit(data, 200, 631)
