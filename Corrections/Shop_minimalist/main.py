# Création des produits
from cart import Cart
from product import Product
from shop import Shop

maki_vege = Product("maki_vege", 1.20)
maki_thon = Product("maki_thon", 2.80)
ramen = Product("ramen", 4.80)

chocolat_au_lait = Product("chocolat_au_lait", 2)

cart_maki = Cart("maki")
cart_ramen = Cart("ramen")
cart_chocolate = Cart("chocolate")

print("total maki", cart_maki.total())
print("total ramen", cart_ramen.total())

# Création du magasin Toasushi
shop = Shop("Toasushi")
shop.add_cart(cart_maki)
shop.add_cart(cart_ramen)

# Ajouts
try:
    shop.add_to_cart(product = maki_vege, cart = cart_maki, quantity = 3)
    shop.add_to_cart(maki_thon, cart_maki, 10)
    shop.add_to_cart(maki_thon, cart_maki, 1)
    
    # ajout dans un autre panier 
    shop.add_to_cart(ramen, cart_ramen, 10)
    
    shop.add_to_cart(chocolat_au_lait, cart_chocolate, 1)
    
except Exception as e:
    print(e)
    
print("total maki", cart_maki.total())
print("total ramen", cart_ramen.total())


