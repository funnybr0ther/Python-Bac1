
from numpy import *
from scipy.linalg import solve
from math import factorial

eps = finfo('float').eps

def doublePrime(alpha):
    n = len(alpha)
    x = zeros(n); x[2] = 1
    matrice = zeros((n,n))
    for i in range(n):
        matrice[i] = alpha**i / factorial(i)
    betas = solve(matrice,x)
    print(betas)
    