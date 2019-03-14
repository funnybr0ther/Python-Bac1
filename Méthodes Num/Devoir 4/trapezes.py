from numpy import *
def trapezeEasy(f,a,b,n):
    l = linspace(a,b,n)
    h = l[1]-l[0]
    i = linspace(1,n-1,dtype=int)
    x = f(l)
    u = (h)*sum(x[1:n])
    u += ((l[1]-l[0])/2)*(x[0]+x[n-1])
    return u

def trapezeFun(f,a,b,n,nmax,tol):
    prev = trapezeEasy(f,a,b,n)
    while n*2<nmax:
        if abs(trapezeEasy(f,a,b,n)-trapezeEasy(f,a,b,2*n))<tol:
            return trapezeEasy(f,a,b,2*n), n, abs(trapezeEasy(f,a,b,2*n)-trapezeEasy(f,a,b,n))
        n*=2
    return trapezeEasy(f,a,b,2*n), n, abs(trapezeEasy(f,a,b,2*n)-trapezeEasy(f,a,b,n))