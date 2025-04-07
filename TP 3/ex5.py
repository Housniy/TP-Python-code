# 1. Fonction pour retourner les carrés des éléments d'une liste
def liste_carres(liste):
    return [x**2 for x in liste]

# 2. Tester la fonction avec une liste donnée
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
carres = liste_carres(nombres)

# 3. Afficher la liste des carrés retournée
print("La liste des carrés est :", carres)
