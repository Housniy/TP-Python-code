class Etudiant:
    def __init__(self, nom, age, note):
        self.nom = nom
        self.age = age
        self.note = note

    def afficher_info(self):
        print(f"Nom: {self.nom}, Age: {self.age}, Note: {self.note}")

    @staticmethod
    def calculer_moyenne(etudiants):
        if not etudiants:
            return 0
        total_notes = sum(etudiant.note for etudiant in etudiants)
        return total_notes / len(etudiants)


# Exemple d'utilisation
etudiant1 = Etudiant("youssef", 22, 19)
etudiant2 = Etudiant("soufiane", 23, 17)
etudiant3 = Etudiant("achraf", 21, 15)

# Afficher les informations des étudiants
etudiant1.afficher_info()
etudiant2.afficher_info()
etudiant3.afficher_info()

# Calculer et afficher la moyenne des notes
etudiants = [etudiant1, etudiant2, etudiant3]
moyenne = Etudiant.calculer_moyenne(etudiants)
print(f"Moyenne des notes : {moyenne}")