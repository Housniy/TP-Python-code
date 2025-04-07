# Fonction pour vérifier si un mot est un palindrome
def est_palindrome(mot):
    if mot == mot[::-1]:  
        return True
    else:
        return False

# Tester la fonction avec les mots donnés
mots = ["radar", "python", "level"]

for mot in mots:
    if est_palindrome(mot):
        print(f"Le mot '{mot}' est un palindrome.")
    else:
        print(f"Le mot '{mot}' n'est pas un palindrome.")
