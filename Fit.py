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

def Chi(fitparam, input_databox, interval, guess):
    index = np.arange(guess-interval, guess+interval)
    fit = Gaussian(index, *fitparam)
    out = ((input_databox[guess-interval: guess+interval]-fit)**2/(input_databox[guess-interval: guess+interval])**2)
    return np.sum(out[out < 10**10])

##### ALUMINUM
### Al 55
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Aluminum/02 Aluminum 55 degrees 000.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Aluminum/02 Aluminum 55 degrees 024.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Aluminum/02 Aluminum 55 degrees 006.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Aluminum/02 Aluminum 55 degrees 010.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Aluminum/02 Aluminum 55 degrees 014.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Aluminum/02 Aluminum 55 degrees 020.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Aluminum/02 Aluminum 55 degrees 033.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 55 - Aluminum')
plt.show()

Al_55peak_x = 607
Al_55param = Fit(data, 100, Al_55peak_x)
Al_55chi = Chi(Al_55param[0], data, 100, Al_55peak_x)

### Al 65
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/65/02 Aluminum/02 Aluminum 65 degrees 009.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/65/02 Aluminum/02 Aluminum 65 degrees 017.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/65/02 Aluminum/02 Aluminum 65 degrees 023.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/65/02 Aluminum/02 Aluminum 65 degrees 030.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/65/02 Aluminum/02 Aluminum 65 degrees 037.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 65 - Aluminum')
plt.show()

Al_65peak_x = 637
Al_65param = Fit(data, 100, Al_65peak_x)
Al_65chi = Chi(Al_65param[0], data, 100, Al_65peak_x)

### Al 75
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Aluminum/02 Aluminum 75 degrees 024.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Aluminum/02 Aluminum 75 degrees 030.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Aluminum/02 Aluminum 75 degrees 008.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Aluminum/02 Aluminum 75 degrees 012.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Aluminum/02 Aluminum 75 degrees 021.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Aluminum/02 Aluminum 75 degrees 028.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Aluminum/02 Aluminum 75 degrees 036.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 75 - Aluminum')
plt.show()

Al_75peak_x = 692
Al_75param = Fit(data, 100, Al_75peak_x)
Al_75chi = Chi(Al_75param[0], data, 100, Al_75peak_x)

### Al 85
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/85/02 Aluminum/02 Aluminum 85 degrees 000.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/85/02 Aluminum/02 Aluminum 85 degrees 007.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/85/02 Aluminum/02 Aluminum 85 degrees 018.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/85/02 Aluminum/02 Aluminum 85 degrees 035.Chn')[1]


plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 85 - Aluminum')
plt.show()

Al_85peak_x = 746
Al_85param = Fit(data, 100, Al_85peak_x)
Al_85chi = Chi(Al_85param[0], data, 100, Al_85peak_x)

### Al 95
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Aluminum/02 Aluminum 95 degrees 002.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Aluminum/02 Aluminum 95 degrees 028.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Aluminum/02 Aluminum 95 degrees 007.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Aluminum/02 Aluminum 95 degrees 023.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Aluminum/02 Aluminum 95 degrees 025.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Aluminum/02 Aluminum 95 degrees 037.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 95 - Aluminum')
plt.show()

Al_95peak_x = 830
Al_95param = Fit(data, 100, Al_95peak_x)
Al_95chi = Chi(Al_95param[0], data, 100, Al_95peak_x)

### Al 105
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/105/02 Aluminum/02 Aluminum 105 degrees 003.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/105/02 Aluminum/02 Aluminum 105 degrees 023.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/105/02 Aluminum/02 Aluminum 105 degrees 028.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/105/02 Aluminum/02 Aluminum 105 degrees 038.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 105 - Aluminum')
plt.show()

Al_105peak_x = 930
Al_105param = Fit(data, 100, Al_105peak_x)
Al_105chi = Chi(Al_105param[0], data, 100, Al_105peak_x)

### Al 125
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Aluminum/02 Aluminum 125 degrees 027.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Aluminum/02 Aluminum 125 degrees 036.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Aluminum/02 Aluminum 125 degrees 016.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Aluminum/02 Aluminum 125 degrees 024.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Aluminum/02 Aluminum 125 degrees 030.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Aluminum/02 Aluminum 125 degrees 032.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 125 - Aluminum')
plt.show()

Al_125peak_x = 1133
Al_125param = Fit(data, 100, Al_125peak_x)
Al_125chi = Chi(Al_125param[0], data, 100, Al_125peak_x)

### Al 220
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Aluminum/02 Aluminum 220 degrees 036.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Aluminum/02 Aluminum 220 degrees 039.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Aluminum/02 Aluminum 220 degrees 021.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Aluminum/02 Aluminum 220 degrees 023.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Aluminum/02 Aluminum 220 degrees 031.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Aluminum/02 Aluminum 220 degrees 033.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 220 - Aluminum')
plt.show()

Al_220peak_x = 1350
Al_220param = Fit(data, 100, Al_220peak_x)
Al_220chi = Chi(Al_220param[0], data, 100, Al_220peak_x)

### Al 230
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/230/02 Aluminum/02 Aluminum 230 degrees 005.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/230/02 Aluminum/02 Aluminum 230 degrees 009.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/230/02 Aluminum/02 Aluminum 230 degrees 018.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/230/02 Aluminum/02 Aluminum 230 degrees 024.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 230 - Aluminum')
plt.show()

Al_230peak_x = 1224
Al_230param = Fit(data, 100, Al_230peak_x)
Al_230chi = Chi(Al_230param[0], data, 100, Al_230peak_x)

### Al 240
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Aluminum/02 Aluminum 240 degrees 002.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Aluminum/02 Aluminum 240 degrees 007.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Aluminum/02 Aluminum 240 degrees 015.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Aluminum/02 Aluminum 240 degrees 021.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Aluminum/02 Aluminum 240 degrees 025.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Aluminum/02 Aluminum 240 degrees 032.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 240 - Aluminum')
plt.show()

Al_240peak_x = 1109
Al_240param = Fit(data, 100, Al_240peak_x)
Al_240chi = Chi(Al_240param[0], data, 100, Al_240peak_x)

### Al 250
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/250/02 Aluminum/02 Aluminum 250 degrees 015.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/250/02 Aluminum/02 Aluminum 250 degrees 016.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/250/02 Aluminum/02 Aluminum 250 degrees 019.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/250/02 Aluminum/02 Aluminum 250 degrees 021.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 250 - Aluminum')
plt.show()

Al_250peak_x = 988
Al_250param = Fit(data, 100, Al_250peak_x)
Al_250chi = Chi(Al_250param[0], data, 100, Al_250peak_x)

### Al 260
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Aluminum/02 Aluminum 260 degrees 006.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Aluminum/02 Aluminum 260 degrees 039.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Aluminum/02 Aluminum 260 degrees 000.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Aluminum/02 Aluminum 260 degrees 012.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Aluminum/02 Aluminum 260 degrees 013.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Aluminum/02 Aluminum 260 degrees 029.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 260 - Aluminum')
plt.show()

Al_260peak_x = 879
Al_260param = Fit(data, 100, Al_260peak_x)
Al_260chi = Chi(Al_260param[0], data, 100, Al_260peak_x)

### Al 280
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/280/02 Aluminum/02 Aluminum 280 degrees 003.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/280/02 Aluminum/02 Aluminum 280 degrees 007.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/280/02 Aluminum/02 Aluminum 280 degrees 020.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/280/02 Aluminum/02 Aluminum 280 degrees 027.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/280/02 Aluminum/02 Aluminum 280 degrees 031.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 280 - Aluminum')
plt.show()

Al_280peak_x = 728
Al_280param = Fit(data, 100, Al_280peak_x)
Al_280chi = Chi(Al_280param[0], data, 100, Al_280peak_x)

### Al 300
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Aluminum/02 Aluminum 300 degrees 002.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Aluminum/02 Aluminum 300 degrees 013.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Aluminum/02 Aluminum 300 degrees 017.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Aluminum/02 Aluminum 300 degrees 026.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Aluminum/02 Aluminum 300 degrees 027.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Aluminum/02 Aluminum 300 degrees 032.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Aluminum/02 Aluminum 300 degrees 033.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 300 - Aluminum')
plt.show()

Al_300peak_x = 631
Al_300param = Fit(data, 100, Al_300peak_x)
Al_300chi = Chi(Al_300param[0], data, 100, Al_300peak_x)

### Al 310
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/310/02 Aluminum/02 Aluminum 310 degrees 002.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/310/02 Aluminum/02 Aluminum 310 degrees 013.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/310/02 Aluminum/02 Aluminum 310 degrees 017.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/310/02 Aluminum/02 Aluminum 310 degrees 026.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/310/02 Aluminum/02 Aluminum 310 degrees 027.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/310/02 Aluminum/02 Aluminum 310 degrees 032.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/310/02 Aluminum/02 Aluminum 310 degrees 033.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 310 - Aluminum')
plt.show()

Al_310peak_x = 637
Al_310param = Fit(data, 100, Al_310peak_x)
Al_310chi = Chi(Al_310param[0], data, 100, Al_310peak_x)

###################################################################
###### Copper
### Cu 55
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Copper/02 Copper 55 degrees 004.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Copper/02 Copper 55 degrees 005.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Copper/02 Copper 55 degrees 012.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Copper/02 Copper 55 degrees 013.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Copper/02 Copper 55 degrees 015.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Copper/02 Copper 55 degrees 018.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Copper/02 Copper 55 degrees 019.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 55 - Copper')
plt.show()

Cu_55peak_x = 613
Cu_55param = Fit(data, 100, Cu_55peak_x)
Cu_55chi = Chi(Cu_55param[0], data, 100, Cu_55peak_x)

### Cu 65
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/65/02 Copper/02 Copper 65 degrees 008.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/65/02 Copper/02 Copper 65 degrees 015.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/65/02 Copper/02 Copper 65 degrees 016.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/65/02 Copper/02 Copper 65 degrees 018.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/65/02 Copper/02 Copper 65 degrees 032.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 65 - Copper')
plt.show()

Cu_65peak_x = 637
Cu_65param = Fit(data, 100, Cu_65peak_x)
Cu_65chi = Chi(Cu_65param[0], data, 100, Cu_65peak_x)

### Cu 75
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Copper/02 Copper 75 degrees 001.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Copper/02 Copper 75 degrees 002.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Copper/02 Copper 75 degrees 009.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Copper/02 Copper 75 degrees 013.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Copper/02 Copper 75 degrees 024.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Copper/02 Copper 75 degrees 025.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Copper/02 Copper 75 degrees 035.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 75 - Copper')
plt.show()

Cu_75peak_x = 685
Cu_75param = Fit(data, 100, Cu_75peak_x)
Cu_75chi = Chi(Cu_75param[0], data, 100, Cu_75peak_x)

### Cu 85
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/85/02 Copper/02 Copper 85 degrees 003.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/85/02 Copper/02 Copper 85 degrees 004.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/85/02 Copper/02 Copper 85 degrees 020.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/85/02 Copper/02 Copper 85 degrees 028.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 85 - Copper')
plt.show()

Cu_85peak_x = 752
Cu_85param = Fit(data, 100, Cu_85peak_x)
Cu_85chi = Chi(Cu_85param[0], data, 100, Cu_85peak_x)

### Cu 95
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Copper/02 Copper 95 degrees 009.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Copper/02 Copper 95 degrees 014.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Copper/02 Copper 95 degrees 023.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Copper/02 Copper 95 degrees 027.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Copper/02 Copper 95 degrees 031.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Copper/02 Copper 95 degrees 038.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 95 - Copper')
plt.show()

Cu_95peak_x = 825
Cu_95param = Fit(data, 100, Cu_95peak_x)
Cu_95chi = Chi(Cu_95param[0], data, 100, Cu_95peak_x)

### Cu 105
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/105/02 Copper/02 Copper 105 degrees 003.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/105/02 Copper/02 Copper 105 degrees 007.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/105/02 Copper/02 Copper 105 degrees 025.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/105/02 Copper/02 Copper 105 degrees 033.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 105 - Copper')
plt.show()

Cu_105peak_x = 903
Cu_105param = Fit(data, 100, Cu_105peak_x)
Cu_105chi = Chi(Cu_105param[0], data, 100, Cu_105peak_x)

### Cu 125
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Copper/02 Copper 125 degrees 013.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Copper/02 Copper 125 degrees 017.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Copper/02 Copper 125 degrees 021.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Copper/02 Copper 125 degrees 026.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Copper/02 Copper 125 degrees 027.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Copper/02 Copper 125 degrees 031.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 125 - Copper')
plt.show()

Cu_125peak_x = 1133
Cu_125param = Fit(data, 100, Cu_125peak_x)
Cu_125chi = Chi(Cu_125param[0], data, 100, Cu_125peak_x)

### Cu 135
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/135/02 Copper/02 Copper 135 degrees 009.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/135/02 Copper/02 Copper 135 degrees 015.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/135/02 Copper/02 Copper 135 degrees 022.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/135/02 Copper/02 Copper 135 degrees 033.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 135 - Copper')
plt.show()

Cu_135peak_x = 1284
Cu_135param = Fit(data, 100, Cu_135peak_x)
Cu_135chi = Chi(Cu_135param[0], data, 100, Cu_135peak_x)

### Cu 220
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Copper/02 Copper 220 degrees 010.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Copper/02 Copper 220 degrees 011.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Copper/02 Copper 220 degrees 020.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Copper/02 Copper 220 degrees 028.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Copper/02 Copper 220 degrees 030.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Copper/02 Copper 220 degrees 036.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 220 - Copper')
plt.show()

Cu_220peak_x = 1363
Cu_220param = Fit(data, 100, Cu_220peak_x)
Cu_220chi = Chi(Cu_220param[0], data, 100, Cu_220peak_x)

### Cu 230
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/230/02 Copper/02 Copper 230 degrees 007.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/230/02 Copper/02 Copper 230 degrees 009.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/230/02 Copper/02 Copper 230 degrees 012.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/230/02 Copper/02 Copper 230 degrees 018.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 230 - Copper')
plt.show()

Cu_230peak_x = 1230
Cu_230param = Fit(data, 100, Cu_230peak_x)
Cu_230chi = Chi(Cu_230param[0], data, 100, Cu_230peak_x)

### Cu 240
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Copper/02 Copper 240 degrees 008.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Copper/02 Copper 240 degrees 010.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Copper/02 Copper 240 degrees 013.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Copper/02 Copper 240 degrees 027.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Copper/02 Copper 240 degrees 028.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Copper/02 Copper 240 degrees 036.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 240 - Copper')
plt.show()

Cu_240peak_x = 1103
Cu_240param = Fit(data, 100, Cu_240peak_x)
Cu_240chi = Chi(Cu_240param[0], data, 100, Cu_240peak_x)

### Cu 250
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/250/02 Copper/02 Copper 250 degrees 004.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/250/02 Copper/02 Copper 250 degrees 010.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/250/02 Copper/02 Copper 250 degrees 021.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/250/02 Copper/02 Copper 250 degrees 032.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 250 - Copper')
plt.show()

Cu_250peak_x = 982
Cu_250param = Fit(data, 100, Cu_250peak_x)
Cu_250chi = Chi(Cu_250param[0], data, 100, Cu_250peak_x)

### Cu 260
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Copper/02 Copper 260 degrees 000.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Copper/02 Copper 260 degrees 009.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Copper/02 Copper 260 degrees 011.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Copper/02 Copper 260 degrees 021.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Copper/02 Copper 260 degrees 031.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Copper/02 Copper 260 degrees 036.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 260 - Copper')
plt.show()

Cu_260peak_x = 879
Cu_260param = Fit(data, 100, Cu_260peak_x)
Cu_260chi = Chi(Cu_260param[0], data, 100, Cu_260peak_x)

### Cu 280
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/280/02 Copper/02 Copper 280 degrees 016.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/280/02 Copper/02 Copper 280 degrees 020.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/280/02 Copper/02 Copper 280 degrees 027.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/280/02 Copper/02 Copper 280 degrees 032.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/280/02 Copper/02 Copper 280 degrees 038.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 280 - Copper')
plt.show()

Cu_280peak_x = 722
Cu_280param = Fit(data, 100, Cu_280peak_x)
Cu_280chi = Chi(Cu_280param[0], data, 100, Cu_280peak_x)

### Cu 300
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Copper/02 Copper 300 degrees 003.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Copper/02 Copper 300 degrees 010.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Copper/02 Copper 300 degrees 012.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Copper/02 Copper 300 degrees 017.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Copper/02 Copper 300 degrees 021.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Copper/02 Copper 300 degrees 029.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Copper/02 Copper 300 degrees 035.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 300 - Copper')
plt.show()

Cu_300peak_x = 637
Cu_300param = Fit(data, 100, Cu_300peak_x)
Cu_300chi = Chi(Cu_300param[0], data, 100, Cu_300peak_x)

### Cu 310
data = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/310/02 Copper/02 Copper 310 degrees 005.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/310/02 Copper/02 Copper 310 degrees 009.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/310/02 Copper/02 Copper 310 degrees 021.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/310/02 Copper/02 Copper 310 degrees 022.Chn')[1]
data += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/310/02 Copper/02 Copper 310 degrees 025.Chn')[1]

plt.scatter(np.arange(0, 2048), data)
plt.title('Angle 310 - Copper')
plt.show()

Cu_310peak_x = 583
Cu_310param = Fit(data, 100, Cu_310peak_x)
Cu_310chi = Chi(Cu_310param[0], data, 100, Cu_310peak_x)