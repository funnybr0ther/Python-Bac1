from numpy import *

def hermite(x,X,U,dU):
    interpolations = {}
    print(len(X))
    X = list(X)
    U = list(U)
    dU = list(dU)
    for i in range(1,len(X)):
        h = X[i] - X[i-1]
        interpolations[(X[i-1], X[i])] = lambda y : (U[i]*3*h*(y-X[i-1])**2 - 2*(y-X[i-1])**3)/(h**3) + U[i-1]*(h**3 - 3*h*(y-X[i-1])**2 + 2*(y-X[i-1])**3)/(h**3) + dU[i]*((y-X[i-1])**2)*((y-X[i-1])-h)/h**2 + dU[i-1] * (y-X[i-1])*((y-X[i-1]) - h)**2 / h**2
    solutions = []

    for l in x:
        temp = []
        for j in interpolations:
            if j[0] <= l <= j[1]:
                temp2 = interpolations[j](l)
                temp.append(temp2)
                break
        solutions.append(temp)
    return array(solutions)
