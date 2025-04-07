# 1. Créer une deuxième liste
autres_nombres = [7, 11, 19, 24, 33]

# 2. Fonction pour fusionner deux listes et retourner une nouvelle liste triée
def fusionner_et_trier(liste1, liste2):
    fusion = liste1 + liste2  # Fusion des deux listes
    fusion_triee = sorted(fusion)  # Tri de la liste fusionnée
    return fusion_triee

# 3. Tester la fonction avec les listes 'nombres' et 'autres_nombres'
nombres = [4, 8, 15, 16, 23, 42]
resultat = fusionner_et_trier(nombres, autres_nombres)

# Afficher le résultat
print("La liste fusionnée et triée est :", resultat)
