from account import Account
from bank import Bank

# Création des comptes
accountAlan = Account("Alan", 0)
accountAlice = Account("Alice", 1_200)
accountSocrates = Account("Socrates", 4_000)

# Mise à jour du solde d'Alice
accountAlice.set_balance(2200)

# Création de la banque
bankPostal = Bank("Banque Postale")

# Ajout des comptes (le second ajout d'Alan lèvera une exception)
try:
    bankPostal.set_account(accountAlan)
    bankPostal.set_account(accountAlan)  # Compte déjà existant
except Exception as e: # alias pour récupérer le message d'erreur 
    print(e) # permet d'afficher le message de l'exception

# Ajout d'Alice
try:
    bankPostal.set_account(accountAlice)
except Exception as e:
    print(e)

# Dépôts sur le compte d'Alan
try:
    bankPostal.deposite_amount(accountAlan, 500)
    bankPostal.deposite_amount(accountAlan, 500)
except Exception as e:
    print(e)

# Dépôt sur un compte non enregistré (Socrates n'a pas été ajouté à la banque)
try:
    bankPostal.deposite_amount(accountSocrates, 2000)
except Exception as e:
    print(e)
