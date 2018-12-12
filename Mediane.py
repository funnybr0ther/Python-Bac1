a = 45
b = 77
c = 66
mediane = 0

if a <= b:
    if b <= c:
        if a <= c:
            mediane = c
        else:
            mediane = a 
    else: 
        mediane = a
elif a >= b:
    if b <= c:
        if a <= c:
            mediane = a
        else:
            mediane = c   
else:
    mediane = b
print (mediane)