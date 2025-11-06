# Création des produits
from cart import Cart
from product import Product
from shop import Shop

maki_vege = Product("maki_vege", 1.20)
maki_thon = Product("maki_thon", 2.80)

cart_sushi = Cart("sushi")

# Création du magasin Toasushi
shop = Shop("Toasushi")

shop.add_cart(cart_sushi)

# Ajouts
try:
    shop.add_to_cart(maki_vege, cart_sushi, 3)
    shop.add_to_cart(maki_thon, cart_sushi, 2)
except Exception as e:
    print(e)


