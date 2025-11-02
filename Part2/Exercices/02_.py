class Account:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    @property
    def balance(self):
        """Retourne le solde actuel."""
        return self._balance

    @balance.setter
    def balance(self, value):
        """Permet de définir le solde, avec contrôle."""
        if value < 0:
            raise ValueError("Le solde ne peut pas être négatif.")
        self._balance = value

    def deposit(self, amount):
        """Ajoute un montant au solde."""
        if amount <= 0:
            raise ValueError("Le dépôt doit être positif.")
        self._balance += amount

    def withdraw(self, amount):
        """Retire un montant du solde."""
        if amount <= 0:
            raise ValueError("Le retrait doit être positif.")
        if amount > self._balance:
            raise ValueError("Fonds insuffisants.")
        self._balance -= amount
