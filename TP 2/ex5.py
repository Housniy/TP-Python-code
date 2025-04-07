# 1. Utiliser la méthode « remove » pour supprimer "mer"
Semaine = ['lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim']
Semaine.remove('mer')  # Supprime "mer" de la liste
print("Résultat 1 :", Semaine)  # Affiche ['lun', 'mar', 'jeu', 'ven', 'sam', 'dim']

# 2. Utiliser pop pour supprimer l'élément à l'index 1
mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)  # Supprime l'élément à l'index 1 ('banana')
print("Résultat 2 :", mylist)  # Résultat : ['apple', 'cherry']

# 3. Fonction pour vider une liste
fruits = ['apple', 'banana', 'cherry']
fruits.clear()  # La fonction "clear" permet de vider une liste
print("Résultat 3 :", fruits)  # Résultat : []
