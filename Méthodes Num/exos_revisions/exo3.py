from numpy import *
from numpy.linalg import solve
def func(t,n,uk):
    a = int(t%1);
    b = uk[a-n-1:a-n+3]
    matrix = array([array([k** l for l in range(0,4)]) for k in range(a-n-1,a-n+3)])
    x = solve(matrix,array(b))
    return x[0] + x[1]*t + x[2]*(t**2) + x[3]*(t**3)
print(func(4,6,linspace(-6,6,2*6+1)))