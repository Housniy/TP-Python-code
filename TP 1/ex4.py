import math

# Saisie des rayons
Rg = float(input("Entrez le rayon du grand disque (Rg) : "))
Rp = float(input("Entrez le rayon du trou circulaire (Rp) : "))

# Vérification : Rp doit être inférieur à Rg
if Rp < Rg:
    # Calcul de la surface
    surface = math.pi * (Rg ** 2) - math.pi * (Rp ** 2)
    print(f"La surface du disque découpé est : {surface:.2f}")
else:
    print("Erreur : Le rayon du trou (Rp) doit être inférieur au rayon du grand disque (Rg).")
