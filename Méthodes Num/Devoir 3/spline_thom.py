# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 3
#
# Canevas de départ....
#
# -------------------------------------------------------------------------
# 
# NE PAS AJOUTER D'AUTRES INSTRUCTIONS import / from :-)
#
from numpy import *
from numpy.linalg import solve




def splung(x,h,U):

    n = size(U)
    X = arange(0,n+1)*h


    l = zeros(len(x),dtype=int)
    for j in range(1,n):
        l[X[j]<=x] = j
        
    A = zeros((n,n),dtype=float)
    for i in range(n-1):
        A[i][i-1] = 1
        A[i][i] = 4
        A[i][i+1] = 1
    A[n-1][0]= 1; A[0][n-1]=1; A[n-1][-1] = 4;A[n-1][-2] = 1
    print(A)
    U_matrice = A - diag(linspace(6,6,n),0)
    U_vect = dot(U_matrice,U)
    ddU = solve(A*h*(h/6),U_vect)
    ddU = append(ddU,ddU[0])
    U = append(U,U[0])
    b = X[l+1] - x
    a = x - X[l]
    print(a)
    print(b)
    print(U)
    print(ddU)  
    return b * (ddU[l]/6 * ((b * b)/h - h) + U[l]/h) + a*( (ddU[l+1]/6)*((a*a)/h - h) + U[l+1]/h )


# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 3
#
# Canevas de départ....
#
# -------------------------------------------------------------------------
# 
# NE PAS AJOUTER D'AUTRES INSTRUCTIONS import / from :-)
#
from numpy import *
from numpy.linalg import solve




def spline(x,h,U):

    n = size(U)
    X = arange(0,n+1)*h


    i = zeros(len(x),dtype=int)
    for j in range(1,n):
        i[X[j]<=x] = j
    
    diag1 = diag(linspace(4,4,n),0)
    diag2 = diag(linspace(1,1,n-1),1)
    diag3 = diag(linspace(1,1,n-1),-1)
    A = diag1+diag2+diag3
    A[0][-1] = 1 ; A[n-1][0]= 1


    A = A*(h**2)/6
    U_vect= zeros(n)
    for i in range(n-1):
        U_vect[i]= U[i-1]-2*U[i]+U[i+1]
    U_vect[n-1] = (U[0]-2*U[n-1]+U[n-2])

    ddU = solve(A,U_vect)
    U = append(U,U[0])
    ddU = append(ddU,ddU[0])
    b = (X[i+1]-x)
    a = (x-X[i])
    return b * (ddU[i]/6 * ((b * b)/h - h) + U[i]/h) + a*( (ddU[i+1]/6)*((a*a)/h - h) + U[i+1]/h )