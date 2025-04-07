class Livre :
    def __init__(self,titre,auteur,statut="disponible"):
        self.titre = titre
        self.auteur = auteur
        self.statut = statut
    def __repr__(self):
        return f"'{self.titre}' de {self.auteur} - Statut: {self.statut}"

class Bibliotheque(Livre):
    def __init__(self):
        super().__init__(titre="",auteur="",statut="")
        self.livres = []

    def ajouter_livre(self,livre):
        self.livres.append(livre)
    def emprunter_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre:
                if livre.statut == "disponible":
                    livre.statut = "emprunté"
                    print(f"Le livre {titre}  a été emprunté.")
                else:
                    print(f"Le livre {titre}  est déjà emprunté.")
    def rendre_livre(self,titre):
        for livre in self.livres:
            if livre.titre == titre:
                if livre.statut == "emprunte":
                    livre.statut = "disponible"
                    print(f"Le livre {titre}  a été rendu.")
                else:
                    print(f'Le livre "{titre}" n\'était pas emprunté.')

    def lister_livres(self):
        if not self.livres:
            print("La bibliothèque est vide.")
        else:
            for livre in self.livres:
                if livre.statut == "disponible":
                  print(livre)

livre1 = Livre("python1","auteur1","disponible")
livre2 = Livre("python2","auteur2","emprunte")
livre3 = Livre("python3","auteur3","disponible")

biblio = Bibliotheque()
biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)
biblio.ajouter_livre(livre3)

biblio.emprunter_livre("python1")
biblio.rendre_livre("python3")

biblio.lister_livres()