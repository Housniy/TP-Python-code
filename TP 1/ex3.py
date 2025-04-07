import math

# Saisie du rayon et de la hauteur
rayon = float(input("Entrez le rayon du cône : "))
hauteur = float(input("Entrez la hauteur du cône : "))

# Calcul du volume
volume = (1/3) * math.pi * (rayon ** 2) * hauteur

# Affichage du volume
print(f"Le volume du cône est : {volume:.2f}")
