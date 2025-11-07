from product import Product

class Book(Product):

    def __init__(self, name, price, author):
        super().__init__(name = name, price = price, tva = 0.40)
        self.author = author
        
    