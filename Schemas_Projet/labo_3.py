from numpy import *
import matplotlib.pyplot as plt
from scipy import signal

x = linspace(0,1,10000)
liste_25 = linspace(2.5,2.5,10000)
y = signal.sawtooth(2*pi*x*3, 0.5)
z = linspace(0,0,10000)
l = sin(z*(2*3*pi))
y = y*2.5
y = y+linspace(2.5,2.5,10000)
a = 0
previous = 2
next = 3
"""for i in range(0,10000):
    if y[i-1] <= previous <= y[i] or y[i] <= previous <= y[i-1]:
        a = a
    elif y[i-1] <= next <= y[i] or y[i] <= next <= y[i-1]:
        print(x[i])
        a = abs(a-5)
        temp = previous
        previous = next
        next = temp
        print(str(previous) + "," + str(next))
    z[i] = a
print(y)"""
for i in range(0,10000):
    if y[i] >= 2.5:
        z[i] = 5
    else:
        z[i] = 0
plt.plot(x,y,"b", label = "V_C")
plt.plot(x,z,'--r', label = "V_out")
plt.plot(x,liste_25,'--b', label = "Seuil")
plt.xlabel("t")
plt.ylabel("V")
plt.legend(loc='upper right')
plt.show()
