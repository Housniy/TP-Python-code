# Liste des noms et âges
donnees = [
    "Marouane,22",
    "soufiane,23",
    "oussama,23",
    "hamza,20",
    "zakaria,21"
]
# Écriture des données dans le fichier
with open('Nom_Age.txt', 'w') as fichier:
    for ligne in donnees:
        fichier.write(ligne + "\n")

#stockage des données dans un dictionnaire
dict = {}
# Lecture des données
with open('Nom_Age.txt', 'r') as fichier:
    for ligne in fichier:
        nom, age = ligne.strip().split(',')
        dict[nom] = int(age)
# Affichage du dictionnaire
print(dict)

# ajouter ou modifier
nomMod = input("entrez votre nom : ")
ageMod = int(input("entrez votre age : "))
with open('Nom_Age.txt', 'a') as fichier:
    fichier.write(f"{nomMod},{ageMod}")

print("fichier aprés la modification :")
with open('Nom_Age.txt', 'r') as fichier:
 contenu = fichier.read()
 print(contenu)