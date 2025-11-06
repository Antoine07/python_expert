class Account:
    def __init__(self, name, balance):
        self.name = name              # Nom du compte / titulaire
        self.balance = balance        # Solde du compte (nombre)

    def set_name(self, name):
        self.name = name              # Mise à jour du nom du compte

    def set_balance(self, balance):
        # Vérifie que balance est bien un nombre (int ou float)
        if not isinstance(balance, (int, float)):
            raise TypeError(f"Le montant doit être un nombre, reçu")

        # Ajoute le montant au solde (positif = dépôt, négatif = retrait)
        self.balance += balance
