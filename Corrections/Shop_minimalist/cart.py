class Cart:
    def __init__(self, name):
        self.products = {}  # {product: quantité}
        self.name = name

    def buy(self, product, quantity):
        total = product.price * quantity
        if product.name in self.products:
            self.products[product.name] += total 
            return
        
        self.products[product.name] = total 
           
    def total(self):
        return sum( self.products.values())
