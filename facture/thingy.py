import math
e = 31381800/10**9 + 0.8
def a(k):
    a = 1
    n = 0
    while n<k:
        a *= (1-2*n)/2
        n += 1
    return abs(a)/math.factorial(k)
def wallis(i):
    if i ==0:
        return math.pi/2
    else:
        return (i-1)/i*wallis(i-2)
def calcul_integrale(steps):
    integrale = 0
    for i in range(1,steps):
        integrale = integrale - a(i)*wallis(2*i)*e**(2*i)
        print(integrale)
    return integrale
print(math.pi/2 + calcul_integrale(37))