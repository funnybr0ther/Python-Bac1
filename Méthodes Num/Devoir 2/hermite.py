from numpy import *

def hermite(x,X,U,dU):
    l = zeros(len(x),dtype=int)
    for j in range(1,len(X)-1):
        l[X[j]<=x] = j
    A = (3*(U[l+1] - U[l])/((X[l+1] - X[l])**2)) - ((dU[l+1] + 2*dU[l])/(X[l+1] - X[l]))
    B = -2*(U[l+1] - U[l])/(X[l+1] - X[l])**3 + (dU[l+1] + dU[l])/(X[l+1] - X[l])**2
    interpol = U[l] + (x-X[l])*(dU[l] + (x-X[l])*(A + (x-X[l])*B))
    return interpol
