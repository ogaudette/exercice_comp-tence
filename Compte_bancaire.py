class CompteBancaire:
    def __init__(self, titulaire, numero_compte, solde, historique):
        self.__titulaire = titulaire
        self.__numero_compte = numero_compte
        self.__solde = solde
        self.__historique = historique

    @property
    def titulaire(self):
        return self.__titulaire

    @property
    def numero_compte(self):
        return self.__numero_compte

    @property
    def solde(self):
        return self.__solde

    @property
    def historique(self):
        return str(self.__historique)

    @numero_compte.setter
    def nouv_numero_compte(self, nouv_numero_compte):
        if nouv_numero_compte >= 0:
            return nouv_numero_compte
        self.__numero_compte = nouv_numero_compte

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
        self.__historique = f"Dépôt: +{montant}, Solde: {self.__solde}"

    def retirer(self, montant):
        if self.__solde >= montant > 0:
            self.__solde -= montant
        return f"Retrait : -{montant}, Solde: {self.__solde}"

    def __str__(self):
        return (f"Le propriétaire du Compte Bancaire numéro {self.__numero_compte} est {self.__titulaire}."
                f" Le solde actuel est de {self.__solde}$.")

compte1 = CompteBancaire("Jo", "449", 1400, [])
compte1.retirer(500)

print(compte1.historique)
print(compte1.solde)

