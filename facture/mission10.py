"""
    Un article de facture simple, comprenant un descriptif et un prix.
   
    @author Kim Mens
    @version 18 novembre 2018
    (code adapté du code java de Charles Pecheur)
"""
 
class Article :

    __taux_tva = 0.21   # TVA a 21%
    
    def __init__(self,d,p):
        """
        Cree un article avec description d et prix p.
        """
        self.__description = d
        self.__prix = p

    def description(self):
        """
        Retourne la description de cet article.
        """
        return self.__description
        
    def prix(self):
        """
        Retourne le prix (HTVA) de cet article.
        """
        return self.__prix
        
    def taux_tva(self):
        """
        Retourne le taux de TVA (même valeur pour chaque article)
        """    
        return self.__taux_tva

    def tva(self):
        """
        Retourne la TVA sur cet article
        """    
        return self.prix() * self.taux_tva()
 
    def prix_tvac(self):
        """
        Retourne le prix de l'article, TVA compris.
        """
        return self.prix() + self.tva()

    def __str__(self):
        """
        Retourne un texte decrivant cet article, au format: "{description}: {prix}"
        """
        # WRONG:
        #   return "{0}: {1:.2f}".format(self.get_description, self.get_prix())
        # RIGHT:
        return "{0}: {1:.2f}".format(self.description(), self.prix())

class ArticleReparation(Article):

    def __init__(self,duree):
        self.duree = duree
        self.__description = "Reparation (" + str(duree) + " heures)"

    def prix(self):
        return 20 + 35 * self.duree

class Piece():
    def __init__(self,d,p,w=0,f=False,tr = False):
        self.__description = d
        self.__prix = p
        self.poids = w
        self.fragile = f
        self.tva_reduit = tr

    def __eq__(self,piece2):
        if self.__description == piece2.__description and self.__prix = piece2.__prix:
            return True
        else:
            return False
    def __str__(self):
    """
    Retourne un texte decrivant cet article, au format: "{description}: {prix}"
    """
    string = "{0}: {1:.2f}".format(self.description(), self.prix()) 
    if self.fragile = True:
        return string + "(!)"
    else:
        return string

    
