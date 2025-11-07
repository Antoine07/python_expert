class Cart:
    PRECISION = 2
    
    def __init__(self, name):
        self.products = {}  # {product: quantité}
        self.name = name

    def buy(self, product, quantity):
        total = round(product.price_ttc() * quantity, Cart.PRECISION)
        # get(k, 0) accèder à une clé en initialisant la valeur de la clé si elle n'existe pas 
        self.products[product.name] = self.products.get(product.name, 0) + total
            
    def total(self):
        print(Cart.PRECISION)
        return round( sum( self.products.values()), Cart.PRECISION)
    
