import numpy as np

# 1. Création des tableaux
# a. Tableau 1D contenant les nombres de 0 à 9
tableau_1d = np.arange(10)
print("Tableau 1D :", tableau_1d)

# b. Tableau 2D de dimensions (3, 3) avec des nombres aléatoires entre 0 et 1
tableau_2d = np.random.rand(3, 3)
print("Tableau 2D :\n", tableau_2d)

# c. Tableau 3D de dimensions (2, 3, 4) rempli de zéros
tableau_3d = np.zeros((2, 3, 4))
print("Tableau 3D :\n", tableau_3d)

# 2. Manipulations
# a. Accéder au troisième élément du tableau 1D
troisieme_element = tableau_1d[2]
print("Troisième élément du tableau 1D :", troisieme_element)

# b. Accéder à la deuxième ligne et première colonne du tableau 2D
element_2d = tableau_2d[1, 0]
print("Élément de la deuxième ligne et première colonne du tableau 2D :", element_2d)

# c. Modifier un élément du tableau 3D
tableau_3d[0, 1, 2] = 7  # Exemple : on remplace cet élément par 7
print("Tableau 3D modifié :\n", tableau_3d)

# 3. Récupérations
# a. Les trois premiers éléments du tableau 1D
trois_premiers = tableau_1d[:3]
print("Les trois premiers éléments du tableau 1D :", trois_premiers)

# b. La dernière colonne du tableau 2D
derniere_colonne = tableau_2d[:, -1]
print("Dernière colonne du tableau 2D :", derniere_colonne)
