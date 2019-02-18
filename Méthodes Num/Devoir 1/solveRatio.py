from numpy import *
from numpy.linalg import solve


def interpolation(X,U,x):
    n = (len(X)-1)//2
    new_matrix = []
    for l in X:
        line = array([e**(1j*l*i) for i in range(-n,n+1)])
        new_matrix.append(line)
    b = real(solve(array(new_matrix), U))
    uh = []
    for i in x:
        line = array([e**(1j*l*i) for l in range(-n,n+1)])
        uh.append(dot(b,line))
    return real(array(uh))
