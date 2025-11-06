class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}            # Dictionnaire {nom_compte: objet_compte}
        self.overdraf = 500           # Découvert autorisé (limite)

    def set_account(self, account):
        # On vérifie si le compte existe déjà dans la banque
        if account in self.accounts.values():
            raise Exception(f"Le compte {account.name} existe déjà")
        
        # On ajoute le compte en utilisant son nom comme clé
        self.accounts[account.name] = account

    def deposite_amount(self, account, amount):
        amount = abs(amount)  # Dépôt toujours considéré comme positif

        # Vérification de l'existence du compte
        if account not in self.accounts.values():
            raise Exception(f"Le compte {account.name} n'existe pas")

        # Vérification du découvert maximal avant dépôt (logique actuelle)
        if self.accounts[account.name].balance > self.overdraf:
            raise Exception("Découvert atteint")

        # Augmentation du solde du compte
        self.accounts[account.name].balance += amount

    def withdraw_amount(self, account, amount):
        # Vérification de l'existence du compte
        if account not in self.accounts.values():
            raise Exception("Ce compte n'existe pas")

        # Calcul du solde après retrait
        total = account.balance - abs(amount)

        # Vérification du découvert autorisé
        if abs(total) > self.overdraf:
            raise Exception("Découvert atteint")

        # Mise à jour du solde
        self.accounts[account.name].balance = total

    def total(self):
        # Retourne la somme de tous les soldes des comptes de la banque
        return sum(a.balance for a in self.accounts.values())

    def total_account(self, account):
        # Vérification que le compte existe avant d'accéder à son solde
        if account not in self.accounts.values():
            raise Exception(f"Le compte {account.name} n'existe pas")

        return self.accounts[account.name].balance
