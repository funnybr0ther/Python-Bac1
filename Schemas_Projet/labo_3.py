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
y = y*0.2
y = y+linspace(2,2,10000)
state = 5
for i in range(0,9999):
    if y[i+1]-y[i]>0:
        state = 5
    else:
        state = 0
    z[i] = state
plt.plot(x,z,'--r', label = "V_in 1")
plt.plot(x,5-z,'--b', label = "V_in 2")
plt.plot(x,(z-2.5)*1.8,'c', label = "V_out")
plt.xlabel("t")
plt.ylabel("V")
plt.legend(loc='upper right')
axes = plt.gca()
axes.set_xlim([0,1])
axes.set_ylim([-6,6])
plt.savefig(fname="vout.pdf",format="pdf")
plt.show()