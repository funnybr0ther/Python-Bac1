
from numpy import *
from numpy.linalg import solve

def spline(x,h,U):
    n = size(U)
    X = arange(0,n+1)*h
    print(n)
    l = zeros(len(x),dtype=int)
    for j in range(1,n):
        l[X[j]<=x] = j
    matrice = []
    matrice = diag(linspace(4,4,n),0) + diag(linspace(1,1,n-1),-1) + diag(linspace(1,1,n-1),1)
    matrice[0][n-1] = 1
    matrice[n-1][0] = 1
    matriceU = diag(linspace(-2,-2,n),0) + diag(linspace(1,1,n-1),-1) + diag(linspace(1,1,n-1),1)
    matriceU[0][n-1] = 1
    matriceU[n-1][0] = 1
    matriceU *= (h**2)/6
    print(dot(matriceU,U))
    ddU = solve(array(matrice),dot(matriceU,U))
    u = zeros(size(x))    
    for i in range(0,size(x)):
        u[i] = ddU[l[i]-1]*(X[l[i]] - x[i])**3 /(6*h) + ddU[l[i]]*(x[i] - X[l[i]-1])**3 + (U[l[i]-1]/h - ddU[l[i]-1]*h/6)*(X[l[i]] -x[i]) + (U[l[i]]/h - ddU[l[i]]*h/6)*(x[i] - X[l[i]-1])
    return u
