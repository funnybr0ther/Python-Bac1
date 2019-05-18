from numpy import *
from scipy.interpolate import CubicSpline as spline
import matplotlib.pyplot as plt
xh = linspace(-1,1,21)
U = sin(2*pi*xh)
pert = 1.0*10**-4
Upert = U + (-1)**arange(1,22)*pert
x = linspace(-1,1,1000)
uLag = polyval(polyfit(xh,U,20),x)
uLagpert = polyval(polyfit(xh,Upert,20),x)
uSpl = spline(xh,U)(x)
USplpert = spline(xh,Upert)(x)
plt.plot(x,uLag)
plt.show()
plt.plot(x,uLagpert)
plt.show()
plt.plot(x,uSpl)
plt.show()
plt.plot(x,USplpert)
plt.show()