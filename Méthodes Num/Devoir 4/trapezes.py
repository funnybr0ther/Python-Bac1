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
    conteur = 0
    while abs((trapezeEasy(f,a,b,2*n))-prev) < tol and conteur <= nmax:
        prev = trapezeEasy
        conteur += 1
    return prev,conteur, abs(trapezeEasy(f,a,b,2*n)-prev)
def tamere(x):
    return sin(x)
print(trapezeEasy(tamere,0,2*pi,1000))