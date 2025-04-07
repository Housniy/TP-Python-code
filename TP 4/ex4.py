# Liste des noms et notes
notes_etudiants = [
    "soufiane,15",
    "achraf,12",
    "marouane,18",
    "anas,10",
    "khalid,14",
    "youssef,17"
]
# Écriture des données dans le fichier
with open('fichier_notes', 'w') as fichier:
    for ligne in notes_etudiants:
        fichier.write(ligne + "\n")

# Lecture des données
etudiants = {}
with open('fichier_notes', 'r') as fichier:
    for ligne in fichier:
        nom, note = ligne.strip().split(',')
        etudiants[nom] = int(note)
print(etudiants)
# Calcul de la moyenne
moyenne = sum(etudiants.values()) / len(etudiants)
print("la moyenne est : ",moyenne)

#afichage
print("les etudians superieur a la moyenne : ")
for nom,note in etudiants.items():
    if note > moyenne :
        print(f"l'étudiant : {nom} , note : {note}")