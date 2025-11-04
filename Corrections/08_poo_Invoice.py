class Invoice:
    
    def __init__(self, id, amounts):
        self.id = id
        self.amounts = amounts
        
    def total(self):
        return sum(self.amounts)
        
    def __len__(self):
        return len(self.amounts)
    
    def __str__(self):
        # la fonction len appelée avec paramètre self
        # déclenche de manière automatique la fonction dunder __len__
        return f"Total Amount: {self.total()} number amount: {len(self)}"
    
# la création de l'objet on a crée un self propre à cet objet
invoice1 = Invoice(123, [11.8, 19.5, 10]) # self 

print(invoice1) # appel la fonction dunder __str__
print(len(invoice1)) # on le fait également dans la méthode dunder __len__


# la création de l'objet on a crée un self propre à cet objet
invoice2 = Invoice(124, [20, 28]) # self 

print(invoice2) # appel la fonction dunder __str__
print(len(invoice2)) # on le fait également dans la méthode dunder __len__