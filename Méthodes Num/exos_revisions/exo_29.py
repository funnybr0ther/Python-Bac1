from numpy import *
def u(x):
    return pow(x,-0.5)
def compute_basic(i,u,xo,xn):
    basic_list = linspace(xo,xn,2**(i-1) +1)
    computed_list = u(basic_list)
    mult_vector = empty(2**(i-1) +1)
    mult_vector[-1] = 1; mult_vector[0] = 1
    mult_vector[1:-1] = 2
    print(mult_vector)
    return (xn-xo)/(2**i) * dot(mult_vector,computed_list)
def richardson(imax,xo,xn,u):
    matrix = empty((imax,imax))
    for i in range(0,imax):
        matrix[i][0] = compute_basic(i+1,u,xo,xn)
    for j in range(1,imax):
        for i in range(j,imax):
            matrix[i,j] = ((2**j)*matrix[i,j-1] - matrix[i-1,j-1])/(2**j -1)
    return matrix[-1,-1]
print(richardson(6,0,1,u))