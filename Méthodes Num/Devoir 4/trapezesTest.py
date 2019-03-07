# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 4
#
# Script de test
#  Vincent Legat
#
# -------------------------------------------------------------------------
# 


from matplotlib import pyplot as plt
from numpy import *
from trapezes import trapezeEasy,trapezeFun

def u(x):
  return cos(x)
  
a = 0
b = pi/2
n = 10

I = trapezeEasy(u,a,b,n)
errorExact = abs(1.0 - I)
print(" ======= Integral of sinus between 0 and pi/2 = %21.14e " % I)
print("  True error = %14.7e" % errorExact)
print("  Number of intervals = %d" % n)
print("\n")

I,n,errorEst = trapezeFun(u,a,b,n,200000,1e-12)
errorExact = abs(1.0 - I)
print(" ======= Integral of sinus between 0 and pi/2 = %21.14e " % I)
print("  True error = %14.7e" % errorExact)
print("  Est. error = %14.7e" % errorEst)
print("  Number of intervals = %d" % n)



plt.figure("Discovering the trapezoids integration rule :-)")
x = [a,b]
plt.plot(x,u(x),'.k',markersize=5) 
x = linspace(a,b,200)
plt.fill(append(x,[0]),append(u(x),[0]),'xkcd:sky blue')
x = linspace(-pi/2,pi,300)
plt.plot(x,u(x),'-k')
plt.title('Integrating sinus between 0 and pi/2')
plt.gca().axhline(y=0,color='k',linewidth=1.0)
plt.text(0.1,0.1,"I = %6.4f" % I,fontsize=12)
plt.show()