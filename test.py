def hermite(x,X,U,dU):
    interpolations = {}
    print(len(X))
    for i in range(1,len(X)):
        h = X[i] - X[i-1]
        print(type(i))
        interpolations[(X[i-1], X[i])] = lambda x : (U[i]*3*h*(x-X[i-1])**2 - 2*(x-X[i-1])**3)/(h**3) + U[i-1]*(h**3 - 3*h*(x-X[i-1])**2 + 2*(x-X[i-1])**3)/(h**3) + dU[i]*((x-X[i-1])**2)*((x-X[i-1])-h)/h**2 + dU[i-1] * (x-X[i-1])*((x-X[i-1]) - h)**2 / h**2
    solutions = []
    print(interpolations[(2,3)](4))

hermite([1,2,3],[1,2,3],[1,2,3],[1,2,3])
