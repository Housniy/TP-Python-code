import numpy as np

# 1. Tableau aléatoire 5x5 et calculs statistiques
tableau_5x5 = np.random.rand(5, 5)  # Tableau aléatoire (valeurs entre 0 et 1)
print("Tableau 5x5 :\n", tableau_5x5)

# Calculs par ligne
moyenne_lignes = tableau_5x5.mean(axis=1)
ecart_type_lignes = tableau_5x5.std(axis=1)
minimum_lignes = tableau_5x5.min(axis=1)
maximum_lignes = tableau_5x5.max(axis=1)

# Calculs par colonne
moyenne_colonnes = tableau_5x5.mean(axis=0)
ecart_type_colonnes = tableau_5x5.std(axis=0)
minimum_colonnes = tableau_5x5.min(axis=0)
maximum_colonnes = tableau_5x5.max(axis=0)

print("Moyenne par ligne :", moyenne_lignes)
print("Écart-type par ligne :", ecart_type_lignes)
print("Minimum par ligne :", minimum_lignes)
print("Maximum par ligne :", maximum_lignes)

print("Moyenne par colonne :", moyenne_colonnes)
print("Écart-type par colonne :", ecart_type_colonnes)
print("Minimum par colonne :", minimum_colonnes)
print("Maximum par colonne :", maximum_colonnes)

# 2. Tri d'un tableau aléatoire et recherche d'indice
tableau_aleatoire = np.random.rand(10)  # Tableau aléatoire de longueur 10
tableau_tri = np.sort(tableau_aleatoire)  # Tri croissant
indice_element = np.argmax(tableau_aleatoire)  # Indice de la valeur maximale
print("Tableau aléatoire :", tableau_aleatoire)
print("Tableau trié :", tableau_tri)
print("Indice de l'élément maximal :", indice_element)

# 3. Broadcasting : multiplication d'un tableau 1D et 2D
tableau_1d = np.array([1, 2, 3, 4])  # Tableau 1D de longueur 4
tableau_2d = np.random.rand(3, 4)  # Tableau 2D de dimensions (3, 4)

produit = tableau_2d * tableau_1d  # Broadcasting : multiplication élément par élément
print("Tableau 1D :", tableau_1d)
print("Tableau 2D :\n", tableau_2d)
print("Résultat de la multiplication (broadcasting) :\n", produit)
