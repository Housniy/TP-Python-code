# 1. Fonction pour trouver le minimum et le maximum dans une liste
def trouver_min_max(liste):
    min_val = min(liste)
    max_val = max(liste)
    return (min_val, max_val)

# 2. Tester la fonction avec la liste nombres
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultat = trouver_min_max(nombres)

# Afficher le résultat
print("Le minimum et le maximum de la liste sont :", resultat)
