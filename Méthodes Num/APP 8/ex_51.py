from numpy import *
x=linspace(0,1,10000)
u = empty(10000)
u[0] = 0
h = 1/10000
for i in range(0,9999):
    u[i+1] = u[i] + h*sin(x[i+1])
    u[i+1] *= (1/(1-h))
print(u[-1])