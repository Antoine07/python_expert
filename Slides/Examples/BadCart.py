class Cart:
    def __init__(self):
        self.products = []

    def add(self, name, price):
        self.products.append((name, price))

    def total(self):
        return sum(price for _, price in self.products)

    def display(self):
        print("Your cart:")
        for name, price in self.products:
            print(f"- {name}: {price}€")
        print("Total:", self.total())

    def save(self):
        with open("cart.txt", "w") as f:
            for name, price in self.products:
                f.write(f"{name},{price}\n")
            f.write(f"Total,{self.total()}\n")