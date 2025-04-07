import numpy as np

# 1. Création de deux tableaux 1D de longueur 5
tableau1 = np.array([1, 2, 3, 4, 5])
tableau2 = np.array([5, 4, 3, 2, 1])

# Opérations élément par élément
addition = tableau1 + tableau2
soustraction = tableau1 - tableau2
multiplication = tableau1 * tableau2
division = tableau1 / tableau2

print("Addition :", addition)
print("Soustraction :", soustraction)
print("Multiplication :", multiplication)
print("Division :", division)

# 2. Application des fonctions np.sin, np.cos, et np.exp sur un tableau de valeurs entre 0 et π
valeurs = np.linspace(0, np.pi, 5)  # Tableau de valeurs entre 0 et π
sinus = np.sin(valeurs)
cosinus = np.cos(valeurs)
exponentiel = np.exp(valeurs)

print("Valeurs :", valeurs)
print("Sinus :", sinus)
print("Cosinus :", cosinus)
print("Exponentiel :", exponentiel)

# 3. Création d'un tableau d'entiers de longueur 10
tableau_entiers = np.arange(1, 11)

# a. Sélection des éléments pairs
elements_pairs = tableau_entiers[tableau_entiers % 2 == 0]
print("Éléments pairs :", elements_pairs)

# b. Remplacement des éléments impairs par -1
tableau_modifie = np.where(tableau_entiers % 2 == 0, tableau_entiers, -1)
print("Tableau modifié :", tableau_modifie)
