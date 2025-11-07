class Shop:
    def __init__(self, name):
        self.name = name
        self.carts = {} # tous les paniers

    """Le produit le panier et la quantité """
    def add_to_cart(self, product, cart, quantity):
        if cart not in self.carts.values():
            raise Exception("Ce panier n'existe pas !")
        
        cart.buy(product, quantity)
     
    """ Ajoute un panier dans le shop """
    def add_cart(self, cart):
        if cart in self.carts.values():
            raise Exception("Ce panier existe déjà")
        
        self.carts[cart.name] = cart 
