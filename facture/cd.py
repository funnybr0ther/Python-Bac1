class Item :
    def __init__ ( self , author , title , serial ) :
        """
        M é thode d ’ initialisation .
        @pre author et title sont des valeurs de type String
        serial est un entier > 0
        @post Une instance de la classe est cr é ée , et repr é sente un objet ayant
        comme auteur author , comme titre title et comme num é ro de s é rie serial
        """
        self . __author = author
        self . __title = title
        self . __serial = serial
    def __str__ ( self ) :
        return "[" + self.__serial + "]" + self.__author + "," + self.__title 

class CD(Item):
    serial = 100000
    def __init__(self, author, title, duration):
        self.__author = author
        self.__title = title
        self.__duration = duration
    def __str__(self):
        return super().__str__(self.__author, )