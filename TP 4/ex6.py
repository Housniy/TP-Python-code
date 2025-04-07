class carnet_adress :
    def _init_(self):
        self.contact={}
    def ajouter_contact(self,nom,email,tele):
        self.contact[nom] = {
            'email': email,
            'telephone': tele
        }
        print(" les informations sont ajoutees")
    def del_name(self,nom):
        if nom in self.contact:
            del self.contact[nom]
            print("Le nom est suprrime")

    def chercher(self,nom):
            if nom in self.contact:
                print("LE nom est trouver")
            else:
                print(" Introuvable!! ")

    def afficher(self):
        for nom in self.contact:
            print(f"{nom}: {self.contact[nom]}")
    def recordfile(self,filename):
        with open(filename,'w',newline="",encoding="utf-8") as file:
            for nom ,infos in self.contact.items():
                file.write(f"{nom},{infos['email']},{infos}")

ca=carnet_adress()
ca.ajouter_contact("marouane","marouane@gmail.com","1324567")
ca.ajouter_contact("ali",'ali1@gmail.com','123456')
ca.ajouter_contact("mohmed",'mhmd@gmail.com','78932132')

ca.afficher()
ca.del_name('ali')
ca.recordfile("conatct.txt")