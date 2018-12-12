from article import Article

"""
   Classe de test initiale pour la classe Article.
   @author Kim Mens
   @version 18 novembre 2018
"""

class TestArticleInitial :

    articles = [ Article("laptop 15\" 8GB RAM", 743.79),
                 Article("installation windows", 66.11),
                 Article("installation wifi", 45.22),
                 Article("carte graphique", 119.49)
                 ]
    
    @classmethod
    def run(cls) :
        for art in cls.articles :
            print(art)

if __name__ == "__main__":
    TestArticleInitial.run()
