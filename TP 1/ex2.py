#Question 1: Saisir les notes et les coefficients des matières
anglais = float(input("Note Anglais : "))
coeff_anglais = int(input("Coefficient Anglais : "))

physique = float(input("Note Physique : "))
coeff_physique = int(input("Coefficient Physique : "))

maths = float(input("Note Maths : "))
coeff_maths = int(input("Coefficient Maths : "))

svt = float(input("Note SVT : "))
coeff_svt = int(input("Coefficient SVT : "))

# Calcul de la moyenne
total_notes = (anglais * coeff_anglais) + (physique * coeff_physique) + (maths * coeff_maths) + (svt * coeff_svt)

total_coefficients = coeff_anglais + coeff_physique + coeff_maths + coeff_svt

moyenne = total_notes / total_coefficients

# Afficher la moyenne
print("La moyenne des notes est :", moyenne)


#Question 2 : 

# Saisir le budget et le montant des achats
budget = float(input("Budget disponible : "))
achats = float(input("Montant des achats : "))

# Vérification et affichage
if budget >= achats:
    print("Le budget permet de payer les achats.")
else:
    print("Le budget est insuffisant pour payer les achats.")

