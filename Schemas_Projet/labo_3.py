from numpy import *
import matplotlib.pyplot as plt
from scipy import signal

x = linspace(0,1,10000)
liste_25 = linspace(2.5,2.5,10000)
y = signal.sawtooth(2*pi*x*3, 0.5)
z = linspace(0,0,10000)
l = sin(x*(2*3*pi))
y = y*2.5
y = y+linspace(2.5,2.5,10000)
y = y+l
y = y*0.6
y = y+linspace(1,1,10000)
previous = 2
next = 3
for i in range(0,10000):
    if 2.5 > y[i]:
        z[i] = 5
    else:
        z[i] = 0
plt.plot(x,y,'r', label = "V_C")
plt.plot(x,linspace(1,1,10000),'--b',label = "Seuil -")
plt.plot(x,linspace(4,4,10000),'--g',label = 'Seuil +')
plt.xlabel("t")
plt.ylabel("V")
plt.legend(loc='upper right')
axes = plt.gca()
axes.set_xlim([0,1])
axes.set_ylim([0,5])
plt.show()
