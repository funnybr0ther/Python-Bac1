from numpy import *
from numpy.linalg import solve

def spline(X,U,x):
    h = X[1:] - X[:-1]
    h.append(h[0])
    matrice = diag(linspace(4,4,n),0) + diag(linspace(1,1,n-1),-1) + diag(linspace(1,1,n-1),1)
    matrice[0][n-1] = 1
    matrice[n-1][0] = 1
    for i in range(0,n):
        matrice[i][i-1]*= h[i];
#Tant pis