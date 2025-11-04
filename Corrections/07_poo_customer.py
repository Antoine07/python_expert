class Customer:
    def __init__(self, name, address, is_vip = False):
        self.name = name
        self.address = address
        self.is_vip = is_vip

    def upgrade_to_vip(self):
        self.is_vip = True

    def change_status(self):
        self.is_vip = not self.is_vip

    def show(self):
        return {
            "name" : self.name,
            "address" : self.address,
            "is_vip" : self.is_vip
        }
         
c1 = Customer("Alice Martin", "12 rue du Parc, Lyon")
c2 = Customer("Bob Leroy", "5 avenue de la Gare, Nantes", is_vip=True)

c1.show() # standard

print("\n--- Alice devient VIP ---")
c1.upgrade_to_vip() # vip
print("vip", c1.show())
c1.change_status()
print("status", c1.show())

print("\n--- Alice devient Standard ---")
c1.is_vip = False
print(c1.show())