class Product:

    """ On définit une tva par défaut attaché à l'objet"""
    def __init__(self, name, price, tva = 0.2):
        self.name = name
        self.price = price
        self.tva = tva 

    def price_ttc(self):
        return self.price * (1 + self.tva)