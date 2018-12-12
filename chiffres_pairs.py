def chiffres_pairs(n):
    i = 0
    while n//10 !=0:
        n = n//10
        i = i+1
    return(i%2 != 0)
print(chiffres_pairs(0))