personnes = {}
nbr = int(input("entrez le nombre de personne souhaite : "))
for i in range(nbr) :
    cle = input("enter le nom : ")
    val = int((input("enter l'age : ")))
    personnes[cle] = val
print(personnes)
def rechercher_per():
 nom = input("Entrez le nom de la personne à rechercher :  ")
 if nom in personnes:
     print(f"{nom} a {personnes[nom]} ans.")
 else:
     print(f"{nom} n'est pas dans le dictionnaire.")

def supprimer_per():
 nom = input("Entrez le nom de la personne à supprimer : ").strip()
 if nom in personnes:
    del personnes[nom]
    print(f"{nom} a été supprimé du dictionnaire.")
 else:
    print(f"{nom} n'est pas dans le dictionnaire.")

rechercher_per()
supprimer_per()
print(personnes)