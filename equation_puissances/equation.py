solutions = 0
#Guillaume van der Rest et Arthur Vandroogenbroek, groupe 11.68
a = int(input("Valeur de a?")) #Demande à l'utilisateur les exposants de x,y et z
b = int(input("Valeur de b?"))
c = int(input("Valeur de c?"))
max = int(input("Valeur maximale de x,y et z?"))
for x in range (0,max+1): #Teste chaque combinaison de x, y et z entre 1 et la 
    for y in range(0,max+1): #valeur maximale et print ces solutions lorsqu'il en trouve, et ajoute 1 au compteur de solutions
        for z in range (0,max+1): 
            if (x**a) + (y**b) == (z**c):
                print("x=", x,"y=", y,"z=",z)
                solutions += 1 #Compteur de solutions

if solutions == 0:
    print ("Aucune solution trouvée")
else:
    print("Il y a ", solutions,"solutions entières à cette équation")