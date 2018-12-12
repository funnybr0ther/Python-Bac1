import turtle #importe le module turtle
import time #importe le module time
wn = turtle.Screen() 
traceur = turtle.Turtle()
traceur.color("black")
traceur.turtlesize(0.00001) #Rend le dessin plus 'clean' en diminuant la taille de la tortue
traceur.speed(7) #Accélère un peu le tracé 
def type1(col1,col2,col3):
    """
    Dessine un drapeau aux bandes verticales de 3 couleurs différentes
    pre: traceur,couleur des trois bandes verticales col1,col2 et col3, objet "traceur"
    post: réalise un drapeau aux bandes verticales en haut à droite du traceur. Le drapeau a une taille de 300*200, la tortue se retrouve donc 300
    unités vers la droite après le dessin du drapeau.
    """


    def rectangle(color):
        """
        Dessine un rectangle vertical de 100*200 d'une couleur spécifiée
        pre: traceur,color, la couleur du rectangle. Celle-ci doit être valide, càd qu'elle appartienne à la banque de couleurs du module turtle
        post: rectangle de couleur (color) et de taille 100*200, vertical en haut à droite de la tortue.
        """
        traceur.begin_fill()
        traceur.color(color)
        for i in range (1,3):
            traceur.forward(100)
            traceur.left(90)
            traceur.forward(200)
            traceur.left(90)
        traceur.end_fill()
    rectangle(col1)
    traceur.forward(100)
    rectangle(col2)
    traceur.forward(100)
    rectangle(col3)


def type2(col1,col2,col3):
    """
    Dessine un drapeau aux bandes horizontale de 3 couleurs différentes
    pre: traceur,couleur des trois bandes horizontale col1,col2 et col3, objet "traceur"
    post: réalise un drapeau aux bandes verticales en dessous à droite du traceur. Le drapeau a une taille de 300*200, µ
    la tortue se retrouve donc 200 unités vers le bas après le dessin du drapeau.
    """

    def rectangle(color):
        """        
        Dessine un rectangle horizontal de 300*(200/3) d'une couleur spécifiée
        pre: traceur,color, la couleur du rectangle. Celle-ci doit être valide, càd qu'elle appartienne à la banque de couleurs du module turtle
        post: rectangle de couleur (color) et de taille 100*200, vertical en bas à droite de la tortue.
        """
        traceur.begin_fill()
        traceur.color(color)
        for i in range (1,3):
            traceur.forward(300)
            traceur.left(90)
            traceur.forward(200/3)
            traceur.left(90)
        traceur.end_fill()
    rectangle(col1)
    traceur.right(90)
    traceur.forward(200/3)
    traceur.left(90)
    rectangle(col2)
    traceur.right(90)
    traceur.forward(200/3)
    traceur.left(90)
    rectangle(col3)
"""
Dessine, à la suite, un drapeau français, allemand, néérlandais et luxembourgeois en se replaçant à chaque fois au bon endroit.
"""
type1("blue","white","red")  #Français
traceur.penup()                  ###penup() et pendown() permettent de ne pas laisser de trait lorsque la tortue se déplace entre deux drapeaux.
traceur.backward(200)
traceur.right(90)
traceur.forward(200/3)
traceur.left(90)
traceur.pendown()
type2("black","red","yellow") #Allemand
traceur.penup()
traceur.backward(300)
traceur.left(90)            
traceur.forward(400/3)
traceur.right(90)
traceur.pendown()
type2("red","white","navyblue") #Néérlandais
traceur.penup()
traceur.left(90)
traceur.forward(1000/3)
traceur.right(90)
traceur.pendown()
type2("red","white","Light sky blue") #Luxembourg
traceur.penup()
traceur.setposition(-300,-200)
traceur.setheading(0)
traceur.pendown()
time.sleep(3) #Attend trois secondes


def reclange(color):
    """
    Dessine un grand rectangle vertical de 200*400 d'une couleur (color) donnée.
    pre: traceur,color, la couleur du rectangle. Celle-ci doit être valide, càd qu'elle appartienne à la banque de couleurs du module turtle
    post: rectangle de couleur (color) et de taille 200*400, vertical en haut à droite de la tortue. 
    La tortue se retrouve en bas du point de départ de 400 unités
    """
    traceur.begin_fill()
    traceur.color(color)
    for i in range (1,3):
        traceur.forward(200)
        traceur.left(90)
        traceur.forward(400)
        traceur.left(90)
    traceur.end_fill()
reclange("black") #Dessine un rectangle noir
traceur.forward(200) #Puis avance de 200 unités
reclange("yellow") #idem
traceur.forward(200)
reclange("red") #idem, drapeau belge complété
time.sleep(2) #Attend deux secondes.
traceur.penup()
traceur.setposition(-300,-200) #Déplace la tortue en bas à gauche du cadre
traceur.setheading(0)
traceur.pendown()
traceur.begin_fill()
traceur.color("navy blue") #Définit la couleur en bleu pour le drapeau européen
for i in range (1,3): #Créée le rectangle bleu
    traceur.forward(600)
    traceur.left(90)
    traceur.forward(400)
    traceur.left(90)
traceur.end_fill()
traceur.setposition((200/3)+10,-400/3+10) #Place la tortue au début du cercle d'étoiles, au milieu-bas du rectangle bleu
traceur.setheading(0) #Reset l'orientation de la tortue vers la droite.


def etoile(couleuretoile):
    """
    Dessine une étoile à 5 branches où chaque "trait" fait 12 unités.
    pre: traceur,la couleur de l'étoile désirée, couleuretoile, doit être valide, donc appartenir à la banque de couleurs du module turtle.
    post: dessine une étoile autour de l'endroit de départ dans la couleur voulue.
    """
    traceur.setheading(0)
    traceur.begin_fill()
    traceur.color(couleuretoile)
    for i in range (1,6):
        traceur.forward(12)
        traceur.right(180-36)
        traceur.forward(12)
        traceur.left(180-108)
    traceur.end_fill()
    traceur.left(30)

    
def couronne():
    """
    Dessine un cercle de 12 étoiles séparées également, avec un axe de symétrie vertical.
    pre: traceur.
    post: une "couronne" d'étoiles est dessinée et la tortue finit à son point de départ
    """
    for i in range (0,12):
        etoile("yellow")
        traceur.setheading(15+(30*(i+1)))
        traceur.penup()
        traceur.forward(31.058285412*2.5)
        traceur.pendown()
couronne()
wn.mainloop() 