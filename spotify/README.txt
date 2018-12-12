Guillaume van der Rest et Theo Vanden Driessche

Ce programme creee trois classes, Duree, chanson et album. La classe duree contient plusieurs fonctions, en plus de __init__, toSecondes, delta, apres, ajouter, et __str__ qui convertit la duree en h:m:s. toSecondes convertit la duree en secondes, delta calcule la difference entre deux durees, apres qui regarde si ce delta est positif, et ajouter qui ajoute une duree a une autre. La classe chanson cree un objet chanson qui a 3 attributs, l'auteur, le nom et la duree. Elle a deux methodes, __str__ et get_duration. str convertit la chanson sous la forme "TITRE - AUTEUR - DUREE", en utilisant la methode str de l'objet Duree et get_duration retourne la duree de la chanson.

La classe album cree un album de moins de 75 minutes et de moins que 100 chansons. Il a 2 methodes, add, qui ajoute une chanson en verifiant si les conditions de duree sont verifiees, et __str__ qui cree un texte pour l'album en specifiant les chansons dedans.

