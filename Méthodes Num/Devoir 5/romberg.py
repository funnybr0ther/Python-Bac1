from numpy import *

def romberg(f,a,b,n,nmax,tol):
    def trapezeEasy(f,a,b,n):
        X = linspace(a,b,n+1)
        return trapz(f(X),X)
    j = 0
    while n*2**j < nmax:
        j += 1
    I = zeros((j,j))
    I[0][0] = trapezeEasy(f,a,b,n)
    for i in range(1,j):
        I[i][0] = trapezeEasy(f,a,b,n*(2**i))
        if abs(I[i][0] - I[i-1][0])<tol:
            return I[i][0], n*(2**i),abs(I[i][0] - I[i-1][0])
    for i in range(1,len(I[0])):
        for l in range(1,i+1):
            I[i][l] = (2**(2*l)*I[i][l-1] - I[i-1][l-1])/(2**(2*l)-1)
        if abs(I[i][i]-I[i][i-1])<tol:
            return I[i][i],n*(2**(i+1)), abs(I[i][i]-I[i][i-1])
    return I[-1][-1], n*(2**j), abs(I[-1][-1]-I[-1][-2])
