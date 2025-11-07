from book import Book
from cart import Cart

novel = Book("The Little Prince", 8.00, "Antoine de Saint-Exupéry")
manga = Book("One Piece Vol. 1", 6.50, "Eiichiro Oda")

print(manga.price_ttc())

# Redéfinit l'attribut statique pour tous les objets que l'on créera par la suite 
Cart.PRECISION = 0

cart = Cart("Library")

cart.buy(novel, 7)
cart.buy(manga,3)

print(cart.total())
print(cart.products)