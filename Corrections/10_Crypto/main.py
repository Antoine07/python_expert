# tous les scripts dans main.py

# Importer vos différentes classes dans ce fichier avec la syntaxe suivante
# En Python un fichier est considérer comme un module que l'on peut importer dans
# un autre fichier comme suit from le_fichier_sans_extention import ta_class, ta_fonction
from Wallet import Wallet
from Order import Order
from prices import PRICES


# on commence avec un portefeuille vide

# Création du portefeuille de départ
wallet = Wallet(PRICES)
print(wallet.prices)
print("-------")
wallet.add_price("BTC", 65_000)
wallet.add_price("DOGE", 0.12)
print(wallet.prices)
print("-------")
# wallet.remove_price("BTC")
print(wallet.prices)

# Gestion de nos cryptos

# Création d'un gestionnaire d'achat
order = Order(wallet)

# Achats simulés
order.buy("BTC", 0.001)
order.buy("DOGE", 200)

# # Affichage du portefeuille final
# print()
print(wallet)