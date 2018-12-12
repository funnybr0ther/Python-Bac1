import time
from functools import wraps
import turtle
g²lobal mem_dic
mem_dic = {}
alreadyknown = {0: 0, 1: 1} #used in optimized fibonnaci sequence


def time_it(f):
    """
        Prend une fonction en argument et retourner une nouvelle fonction
        Sert de décorateur
    """
    #we could put *args instead of x to handle the case when the function f has multiple parameters
    t1 = 0
    t0 = 0
    def wrapped(*arg):
        t0 = time.clock()
        result = f(*arg)
        t1 = time.clock()
        print("ellapsed time: {0}".format(t1-t0))
        return result
    return wrapped


def memoization(fun, arg):
    """
    Function memoization prennant une fonction en argument et l'argument de la fonction
    """
    if fun not in mem_dic: #check si la function est déja dans le dico
        mem_dic[fun] = {}   #sinon ajoute l'entree
    if arg not in mem_dic[fun]: #check si la valeur est deja dans le dico de la fonction
        mem_dic[fun][arg] = fun(arg) #sinon ajoute cette valeur
    return mem_dic[fun][arg] #retourne la valeur demandeµ
    #TODO Myman, Eat Bread

def memoise(f):
    def new_f(x):
        return memoization(f,x)
    return new_f


@memoise
def fib_rec(n):
    """
      Computes numbers in the Fibonacci sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
      pre:  'n' is natural number (an integer >= 0)
      post: returns the n-th Fibonacci number,
            where fib(0) = 0 and fib(1) = 1
            and any other Fibonacci number is defined
            as the sum of the previous 2 Fibonacci numbers,
            for example: fib(2) = fib(0) + fib(1) = 0 + 1 = 1
    """
    if n <= 1:
        return n
    t = fib_rec(n-1) + fib_rec(n-2)
    return t


def optimize_fib_rec(n):
    """
    Fib récursive avec memoise 
    """
    if n not in alreadyknown:
        new_value = optimize_fib_rec(n-1) + optimize_fib_rec(n-2)
        alreadyknown[n] = new_value
    return alreadyknown[n]


def fib_it(n):
    """
        Fonction itérative de fibonnaci
    """
    a,b,c=0,1,0
    if n == 1:
        return 0
    for i in range(n-1):
        c,a,b=b+a,b,b+a
    return c


def fib_it_cul(n):
    """
        Version de GUIGUI
    """
    compteur = [0,1,1]
    for i in range(n-2):
        compteur.append(compteur[-1] + compteur[-2])
    return compteur[-1]              
            

def fact_mem(n):
    """
    Fonction calculant les factorielle
    """
    if n == 0:
        return 1
    else:
        return n * memoization(fact_mem, n-1)


def fibo_mem(n):
    """
    Utile juste pour calculer plus facile la suite de fibonacci
    """
    return memoization(fib_rec,n)


def exec_time(f,x):
    """
    Fonction juste la pour faire plaisir
    """
    time_it(f)(x)
    return
