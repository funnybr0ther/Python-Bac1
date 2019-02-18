"""
    Une facture, sous forme d'une liste d'articles.
   
    @version 18 novembre 2018
    @author Kim Mens
    (code adapté du code java de Charles Pecheur)
"""

class Facture :

    numero = 0

    def __init__(self, description, articles):
        """
        Crée une facture avec une description (titre) et un liste d'articles.
        """
        self.__reference = description + "Facture no. " + str(numero)
        self.__articles = articles
        numero += 1 
    def description(self):
        """
        Retourne la description de cette facture.
        """
        return self.__reference

    def articles(self):
        """
        Retourne la liste des articles de cette facture.
        """
        return self.__articles
        
    def __str__(self):
        """
        Retourne la représentation string d'une facture, à imprimer avec la méthode print().
        """
        s = self.entete_str()
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.articles() :
            s += self.article_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_str(totalPrix, totalTVA)
        return s

    def entete_str(self):
        """
        Imprime l'entête de la facture, comprenant le descriptif et les têtes de colonnes.
        """
        e = "Facture " + self.description() + "\n"
        e += self.barre_str()
        e += "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","prix HTVA","TVA","prix TVAC")
        e += self.barre_str()
        return e

    def barre_str(self):
        """
        Retourne un string représentant une barre horizontale sur la largeur de la facture.
        """
        b = ""
        barre_longeur = 83
        for i in range(barre_longeur):
            b += "="
        return b + "\n"
x
    def article_str(self, art):
        """
        Retourne un string correspondant à une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.prix(), art.tva(), art.prix_tvac())
    
    def totaux_str(self, prix, tva):
        """
        Retourne un string représentant une ligne de facture avec les totaux prix et tva, à imprimer en bas de la facture
        b = self.barre_str()
        """
        b += "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format("T O T A L", prix, tva, prix+tva)
        b += self.barre_str()
        return b
        
    # This method needs to be added during Etape 4 of the mission
    def nombre(self, pce) :
        """
        Retourne le nombre d'exemplaires de la pièce pce dans la facture, en totalisant sur tous les articles qui concernent cette pièce.
        """


    # This method needs to be added during Etape 5 of the mission
    def livraison_str(self):
        """
        Cette méthode est une méthode auxiliaire pour la méthode printLivraison
        """

facture = Facture("oui", "ta mère")