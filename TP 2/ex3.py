# 1. Créer une liste de matières et afficher la liste
matieres = ["Anglais", "Physique", "Maths", "Svt"]
print("Liste des matières :", matieres)

# 2. Ajouter deux nouvelles matières à la liste et afficher la liste
matieres.append("Histoire")
matieres.append("Geographie")
print("Liste des matières après ajout :", matieres)

# 3a. Afficher les 4 premiers éléments de la liste
print("Les 4 premiers éléments de la liste :", matieres[:4])

# 3b. Afficher les 3 derniers éléments de la liste
print("Les 3 derniers éléments de la liste :", matieres[-3:])

# 3c. Afficher 3 éléments depuis le second indice
print("3 éléments à partir du second indice :", matieres[2:5])
