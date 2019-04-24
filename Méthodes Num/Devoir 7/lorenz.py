
from numpy import *
def compute_func(funcs):

    return array([10*funcs[1]-10*funcs[0],28*funcs[0]-funcs[1]-funcs[0]*funcs[2],funcs[0]*funcs[1]-(8/3)*funcs[2]])


def lorenz(Tstart,Tend,Ustart,n):

    matrix = zeros((n+1,3))
    matrix[0] = Ustart
    T = linspace(Tstart,Tend,n+1)
    h = T[1]-T[0]

    for i in range(1,n+1):
        K_1=compute_func(matrix[i-1])
        K_2=compute_func(matrix[i-1]+(h/2)*K_1)
        K_3=compute_func(matrix[i-1]+(h/2)*K_2)
        K_4=compute_func(matrix[i-1]+h*K_3) 
        matrix[i] = matrix[i-1] + (h/6)*(K_1 + 2*K_2 + 2*K_3 + K_4)
    return T,matrix