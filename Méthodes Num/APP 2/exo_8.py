from numpy import *
from scipy.interpolate import CubicSpline as spline
X = sin(linspace(0,3,4)*pi / 6)
Y = cos(linspace(0,3,4)* pi /6)
print(X)
X = array(X)
Y = array(Y)

uSpline1 = spline(X,Y)(linspace(1975,2000,150))

import matplotlib
from matplotlib import pyplot as plt

plt.plot((linspace(1975,2000,150)),uSpline1,'-b',label='spline sur les 10 premiers point')

plt.legend(loc='upper right')
plt.show()
