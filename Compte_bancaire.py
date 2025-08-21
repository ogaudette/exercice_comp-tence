class CompteBancaire:
    def __init__(self, titulaire, numero_compte, solde_initial=0):
        self.__titulaire = titulaire
        self.__numero_compte = numero_compte
        self.__solde = solde_initial
        self.__historique = []

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

    @solde.setter
    def solde(self, montant):
        if not isinstance(montant, (int, float)):
            raise TypeError("solde pas nombre")
        if montant < 0:
            raise ValueError("solde négatif")
        self.__solde = montant
        self.__historique.append(f"modification solde: {montant}")

    @numero_compte.setter
    def nouv_numero_compte(self, nouv_numero_compte):
        if nouv_numero_compte >= 0:
            return nouv_numero_compte
        self.__numero_compte = nouv_numero_compte

    def deposer(self, montant):
        if not isinstance(montant, (int, float)):
            raise TypeError("montant doit être un nombre")
        if montant < 0:
            raise ValueError("montant négatif")
        self.__solde += montant
        self.__historique.append(f"Dépôt: +{montant}, Solde: {self.__solde}")

    def retirer(self, montant):
        if not isinstance(montant, (int, float)):
            raise TypeError("montant doit être un nombre")
        if montant < 0:
            raise ValueError("montant négatif")
        if montant > self.__solde:
            raise ValueError("Solde insuffisant")
        self.__solde -= montant
        self.__historique.append(f"Retrait : -{montant}, Solde: {self.__solde}")

    def __str__(self):
        return (f"Le propriétaire du Compte Bancaire numéro {self.__numero_compte} est {self.__titulaire}."
                f" Le solde actuel est de {self.__solde}$.")

compte1 = CompteBancaire("Jo", "449", 1400)
compte1.retirer(500)

print(compte1.historique)
print(compte1.solde)

