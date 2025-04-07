# Demande à l'utilisateur de saisir une phrase
phrase = input("Entrez une phrase : ")

longueur = len(phrase)

# Affiche la première ou la seconde moitié selon la parité
if longueur % 2 == 0:  # Si la longueur est paire
    print("La longueur de la phrase est paire.")
else:  # Si la longueur est impaire
    print("La longueur de la phrase est impaire.")
