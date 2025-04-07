# 1. Fonction pour extraire les nombres pairs
def extraire_pairs(liste):
    return [x for x in liste if x % 2 == 0]

# 2. Tester la fonction avec une liste donnée
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nombres_pairs = extraire_pairs(nombres)

# 3. Afficher la liste des nombres pairs
print("Les nombres pairs sont :", nombres_pairs)
