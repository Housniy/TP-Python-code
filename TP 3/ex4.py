# Fonction pour vérifier si un élément existe ou non dans une liste
def element_existe(liste, element):
    if element in liste:
        print(f"L'élément {element} existe dans la liste.")
    else:
        print(f"L'élément {element} n'existe pas dans la liste.")

# Tester la fonction avec les éléments 15 et 50 dans la liste nombres
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]

# Test avec l'élément 15
element_existe(nombres, 15)

# Test avec l'élément 50
element_existe(nombres, 50)
