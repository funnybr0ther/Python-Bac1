
from numpy import *
from numpy.linalg import solve

def spline(x,h,U):
   n = size(U)
   X = arange(0,n+1)*h

   i = zeros(len(x),dtype=int)
   for j in range(1,n):
      i[X[j]<=x] = j
   matrice = diag(linspace(4,4,n),0) + diag(linspace(1,1,n-1),-1) + diag(linspace(1,1,n-1),1)
   matrice[0][n-1] = 1
   matrice[n-1][0] = 1
   matriceU = matrice - diag(linspace(6,6,n),0)
   ddU = solve(matrice*h*(h/6),dot(matriceU,U))
   ddU = append(ddU,ddU[0])
   U = append(U,U[0])
   return (X[i+1] - x) * (ddU[i]/6 * (((X[i+1] - x) * (X[i+1] - x))/h - h) + U[i]/h) + (x - X[i])*( (ddU[i+1]/6)*(((x - X[i])*(x - X[i]))/h - h) + U[i+1]/h )