from numpy import *
from numpy.linalg import solve


def interpolation(X,U,x):
    return real(array([dot(solve(array([array([e**(1j*l*i) for i in range(-((len(X)-1)//2),((len(X)-1)//2)+1)]) for l in X]), U),array([e**(1j*l*i) for l in range(-((len(X)-1)//2),((len(X)-1)//2)+1)])) for i in x]))
