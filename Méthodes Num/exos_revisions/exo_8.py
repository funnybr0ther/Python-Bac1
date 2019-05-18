from scipy.interpolate import CubicSpline
from numpy import *
import matplotlib.pyplot as plt
a = CubicSpline(linspace(0,12,12)*pi/6,sin(linspace(0,12,12)*pi/6))
b = CubicSpline(linspace(0,12,12)*pi/6,cos(linspace(0,12,12)*pi/6))
plt.plot(a(linspace(0,12,1000)*pi/6), b(linspace(0,12,1000)*pi/6))
plt.show()