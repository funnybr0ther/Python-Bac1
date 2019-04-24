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
    gamma = (dot(betas,alpha**n/factorial(n)))
    if not abs(gamma)<=dot(alpha**n,betas)*sum(abs(dot(matrice,betas)-x)) and not abs(gamma)<=10**10:
        return betas,1/gamma,n-2
    else:
        return betas,1/dot(betas,alpha**(n+1)/factorial(n+1)),n-1