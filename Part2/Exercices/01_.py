class Customer:
    def __init__(self, name, address, is_vip=False):
        self.name = name
        self.address = address
        self.is_vip = is_vip

    def upgrade_to_vip(self):
        """Passe le client en statut VIP."""
        self.is_vip = True

    def show(self):
        """Affiche les informations du client."""
        status = "VIP" if self.is_vip else "Standard"
        print(f"Client : {self.name} | Adresse : {self.address} | Statut : {status}")
