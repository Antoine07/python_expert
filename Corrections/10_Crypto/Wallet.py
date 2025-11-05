class Wallet:
    def __init__(self, prices, balance = 1_000):
        self.prices = prices # dictionnaire
        self.balance = balance
        self.inventory = {} # dictionnaire 
        
    def add_price(self, symbol, value):
        if symbol not in self.prices:
            self.prices[symbol] = value
            print(f"Ajout du nouveau symbol {symbol}" )
        else:
            print(f"Ce symbol existe déjà", symbol)
            
    def remove_price(self, symbol):
        if symbol in self.prices:
            del self.prices[symbol]
            print(f"Suppression du symbol {symbol}" )
            
    def __str__(self):
        return f"balance : {self.balance} total: {round( sum(self.inventory.values()),10)}"