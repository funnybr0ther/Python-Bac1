
from numpy import *
"""

def lorenz(Tstart,Tend,Ustart,n):

    matrix = zeros((n+1,3))
    matrix[0] = Ustart
    T = linspace(Tstart,Tend,n+1)
    h = T[1]-T[0]


    def compute_func(funcs):

        return array([10*funcs[1]-10*funcs[0],28*funcs[0]-funcs[1]-funcs[0]*funcs[2],funcs[0]*funcs[1]-(8/3)*funcs[2]])

    for i in range(1,n+1):
        K_1=compute_func(matrix[i-1])
        K_2=compute_func(matrix[i-1]+(h/2)*K_1)
        K_3=compute_func(matrix[i-1]+(h/2)*K_2)
        K_4=compute_func(matrix[i-1]+h*K_3) 
        matrix[i] = matrix[i-1] + (h/6)*(K_1 + 2*K_2 + 2*K_3 + K_4)
    return T,matrix
"""
def F(u):

    der=empty(3)

    der[0]=10*(-u[0]+u[1])

    der[1]=u[0]*28-u[2]*u[0]-u[1]

    der[2]=u[0]*u[1]-8/3*u[2]
    

   

    return der

 

def lorenz(Xstart,Xend,Ustart,n):

    h=(Xend-Xstart)/n

    X = linspace(Xstart,Xend,n+1)

    U = empty((n+1,3))

    U[0,:]=array(Ustart)

    for i in range(1,n+1):

        K1=F(U[i-1,:])

        K2=F(U[i-1,:]+(h*K1)/2)

        K3=F(U[i-1,:]+(h*K2)/2)

        K4=F(U[i-1,:]+h*K3)

        U[i,:]=U[i-1,:]+(h*(K1+2*K2+2*K3+K4))/6   

    return X,U