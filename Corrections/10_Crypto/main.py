# tous les scripts dans main.py

# Importer vos différentes classes dans ce fichier avec la syntaxe suivante
# En Python un fichier est considérer comme un module que l'on peut importer dans
# un autre fichier comme suit from le_fichier_sans_extention import ta_class, ta_fonction
from Wallet import Wallet
from Order import Order

prices = {}  # on commence avec un portefeuille vide

# Création du portefeuille de départ
wallet = Wallet(prices)

# Création d'un gestionnaire d'achat
order = Order(wallet)

# Achats simulés
order.buy("BTC", 65000, 0.01)
order.buy("ETH", 3500, 0.2)
order.buy("DOGE", 0.12, 50)

# Affichage du portefeuille final
print()
print(wallet)