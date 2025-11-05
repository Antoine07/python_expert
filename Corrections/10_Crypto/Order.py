class Order:
    def __init__(self, wallet):
        self.wallet = wallet
        
    def buy(self, symbol, quantity):
        # on vérifie si la crypto est dans notre Wallet
        if symbol in self.wallet.prices:
            # On calcule combien la crypto va nous couter
            cost = round( quantity * self.wallet.prices[symbol], 2)
            # On vérifie si on peut l'acheter
            if cost < self.wallet.balance:
                # On met à jour notre balance 
                self.wallet.balance -= round(cost, 2) 
                # on vérifie si on a déjà cette crypto ou pas et on stock
                if symbol in self.wallet.inventory:
                    self.wallet.inventory[symbol] += quantity 
                else:
                    self.wallet.inventory[symbol] = quantity 
                # bilan de l'achat 
                print(f"vous avez payer :{cost} pour obtenir {quantity} de {symbol}")
            else:
                # achat impossible
                print(f"Vous n'avez pas assez d'argent pour acheter {symbol}")
        else:
            # achat impossible car pas dans votre Wallet
            print(f"Vous n'avez pas ce symbol {symbol}")
            