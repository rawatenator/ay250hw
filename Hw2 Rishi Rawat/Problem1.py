##RISHI RAWAT

import numpy as np
import random as rand
import scipy as sp
import matplotlib.pyplot as plt
import scipy.optimize as opt
from scipy.interpolate import UnivariateSpline


def function(x,k):
    return k[0]**(k[1] * x) + k[2]

def residuals(k, data_y_noise, data_x):
    error =  data_y_noise - function(data_x, k)
    return error



####PLOT 1: original f(x),  DATA, Regression(least sq)
plt.figure()

data_x = np.random.uniform(0,4.00000000000000001,20)
data_x.sort()
constants = [2.,-.75,.1]
data_y = function(data_x,constants)
plt.plot(data_x, data_y, label = 'original f(x)')  #ploting the original f(x)



data_y_noise = data_y + .1 * np.random.randn(data_y.size)
plt.plot(data_x, data_y_noise, "bo", label = ' data') #plotting data w/noise



kbestfit = opt.leastsq(residuals, constants, args=(data_y_noise,data_x), full_output = 1)
            #Making the regression: the best parameters should now be in kbestfit[0]


plt.plot(data_x,function(data_x,kbestfit[0]),label = "lin reg")
plt.legend()#plotting complete

plt.title('LIN REG')











####PLOT 2: Polynomial REGRESSIONS FOR NOISY DATA
plt.figure()



plt.plot(data_x, data_y, label = 'original f(x)')  #ploting the original f(x)

plt.plot(data_x, data_y_noise, "bo", label = ' data') #plotting data w/noise
plt.legend()


order2polynom = sp.polyfit(data_x,data_y_noise,0)
order2y = sp.polyval(order2polynom,data_x)
plt.plot(data_x, order2y, label = '0 order polynomial regression, no noise') #0th order polynomial regression:

linRegnoise = sp.polyfit(data_x,data_y_noise,1)
linRegnoise_y = sp.polyval(linRegnoise,data_x)
plt.plot(data_x,linRegnoise_y, label = '1st order poly') #1st order -polyfit:

order2polynomnoise = sp.polyfit(data_x,data_y_noise,2)
order2ynoise = sp.polyval(order2polynomnoise,data_x)
plt.plot(data_x, order2ynoise, label = '2nd order regression, noise') #2nd order -polyfit

plt.legend()#plotting complete
plt.title('PolyFITS')






####PLOT 3: SPLINES
plt.figure()



plt.plot(data_x, data_y, label = 'original f(x)')  #ploting the original f(x)

plt.plot(data_x, data_y_noise, "bo", label = ' data') #plotting data w/noise
plt.legend()


s = UnivariateSpline(data_x,data_y_noise,k=3)
plt.plot(data_x,s(data_x), label = "spline, 3rd order")

s = UnivariateSpline(data_x,data_y_noise,k=2)
plt.plot(data_x,s(data_x), label = "spline, 2rd order")

s = UnivariateSpline(data_x,data_y_noise,k=1)
plt.plot(data_x,s(data_x), label = "spline, 1st order")

plt.title('SPLINES')
plt.legend()
plt.show()


