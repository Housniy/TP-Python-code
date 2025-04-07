# Partie 1 : Fonction pour calculer la somme des éléments d'une liste
def somme_liste(liste):
    return sum(liste)

# Partie 2 : Fonction pour calculer la moyenne des éléments d'une liste
def moyenne_liste(liste):
    return sum(liste) / len(liste)

# Partie 3 : Utiliser les fonctions sur une liste de nombres
nombres = [4, 8, 15, 16, 23, 42]
somme = somme_liste(nombres)
moyenne = moyenne_liste(nombres)

# Afficher les résultats
print("La somme des éléments de la liste est :", somme)
print("La moyenne des éléments de la liste est :", moyenne)
