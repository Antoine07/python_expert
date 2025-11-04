class Order:
    def __init__(self, order_id, products):
        self.order_id = order_id
        self.products = products  # liste de Product

    def total(self):
        return sum(p.price for p in self.products)

    def __len__(self):
        return len(self.products)

    def __str__(self):
        return f"Order {self.order_id} – {len(self)} items – total {self.total():.2f}€"

    # se déclenche quand on fait un in avec l'objet
    def __contains__(self, product_name):
        # print(product_name)
        return any(p.name == product_name for p in self.products)
    
class Product:
     def __init__(self, name, price):
        self.name = name
        self.price = price  

products = [ Product("Brompton", 1500), Product("Mac Book Pro M4", 3000) ]
command = Order(123, products)

print(command.total())

print( len(command) )
print( command )
print("Brompton" in command)
print("Apple" in command)