

class Product:
    TVA = 0.2 # variable statique propre à la classe et pas l'objet
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def price_ttc(self):
        return self.price * (1 + Product.TVA)
    
class Book(Product):
    TVA = 0.12
    # todo 