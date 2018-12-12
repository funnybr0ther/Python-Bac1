def recursive_9(n):
    if n < 9:
        return False
    if n == 9:
        return True
    else:
        return recursive_9(cucu(n))
def cucu(n):
    compteur = 0
    a = str(n)
    for i in a:
        compteur += int(i)
    return compteur
print(recursive_9(97))
