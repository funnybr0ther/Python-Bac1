from numpy import *
import matplotlib.pyplot as plt
from numpy.linalg import inv
from numpy.linalg import lstsq
x_i = linspace(0,10,150)
u_i = x_i**2
matrice = array([array([1,i]) for i in x_i])
coeff = lstsq(matrice, u_i)
inter = lambda x: coeff[0][0]+ coeff[0][1]*x
x = linspace(0,10,150)
plt.plot(x, x**2, 'r')
plt.plot(x, inter(x), 'b')
print(abs((1/3)**2 - coeff[0][0] - coeff[0][1]*(1/3)))
plt.show()
