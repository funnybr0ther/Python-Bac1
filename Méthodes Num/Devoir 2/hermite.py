from numpy import *

def hermite(x,X,U,dU):
    interpolations = {}
    for i in range(1,len(X)):
        h_i = X[i] - X[i-1]
        interpolations[(X[i-1], X[i])]=lambda x : (U[i]*3*h_i*(x-X[i-1])**2 - 2*(x-X[i-1])**3)/(h_i**3) + U[i-1]*(h_i**3 - 3*h_i*(x-X[i-1])**2 + 2*(x-X[i-1])**3)/(h_i**3) + dU[i]*((x-X[i-1])**2)*((x-X[i-1])-h_i)/h_i**2 + dU[i-1] * (x-X[i-1])*((x-X[i-1]) - h_i)**2 / h_i**2
    solutions = []
    for i in x:
        temp = []
        for j in interpolations:
            if j[0] <= i <= j[1]:
                temp.append(interpolations[j](i))
            solutions.append(array(temp))
    return array(solutions)
