# 1. Modifier l'élément à l'index 0 et afficher l'élément à l'index 1
mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print("Résultat 1 :", mylist[1])  # Affiche 'banana'

# 2. Modifier la valeur de "apple" à "kiwi"
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print("Résultat 2 :", fruits)  # Affiche ['kiwi', 'banana', 'cherry']

# 3. Remplacer l'élément à l'index 1 par "kiwi" et "mango", puis afficher l'élément à l'index 2
mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print("Résultat 3 :", mylist[2])  # Affiche 'mango'

# 4. Insérer "orange" au début de la liste et afficher l'élément à l'index 1
mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print("Résultat 4 :", mylist[1])  # Affiche 'apple'

# 5. Ajouter "orange" à la fin de la liste via la fonction append
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("Résultat 5 :", fruits)  # Affiche ['apple', 'banana', 'cherry', 'orange']

# 6. Insérer "lemon" à la seconde position
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print("Résultat 6 :", fruits)  # Affiche ['apple', 'lemon', 'banana', 'cherry']
