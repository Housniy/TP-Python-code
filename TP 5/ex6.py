import numpy as np

ventes = np.random.randint(100, 1000, size=(12, 3))

# Total des ventes par produit
total_ventes = ventes.sum(axis=0)
print("Total des ventes :", total_ventes)

# Moyenne des ventes mensuelles par produit
moyenne_ventes = ventes.mean(axis=0)
print("Moyenne des ventes :", moyenne_ventes)

# Mois avec ventes maximales par produit
mois_max = ventes.argmax(axis=0)
print("Mois des ventes maximales :", mois_max + 1)

# Croissance mensuelle en pourcentage
croissance = np.diff(ventes, axis=0) / ventes[:-1] * 100
print("Croissance mensuelle (%) :\n", croissance)

# Mois avec la plus forte croissance
mois_croissance_max = croissance.argmax(axis=0)
print("Mois avec la plus forte croissance :", mois_croissance_max + 2)

# Somme des ventes mensuelles tous produits confondus
somme_mensuelle = ventes.sum(axis=1)
print("Somme des ventes mensuelles :", somme_mensuelle)
