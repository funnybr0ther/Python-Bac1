from numpy import *
from scipy.interpolate import CubicSpline as spline
X = [1975,1980,1985,1990]
Y = [70.2,70.2,70.3,71.2]
print(X)
X = array(X)
Y = array(Y)

uSpline1 = spline(X,Y)(linspace(1975,2000,150))

import matplotlib
from matplotlib import pyplot as plt

plt.plot((linspace(1975,2000,150)),uSpline1,'-b',label='spline sur les 10 premiers point')

plt.legend(loc='upper right')
plt.show()
