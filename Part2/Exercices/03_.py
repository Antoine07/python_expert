class Invoice:
    def __init__(self, invoice_id):
        self.invoice_id = invoice_id
        self.amounts = []

    def add_amount(self, amount):
        """Ajoute un montant à la facture."""
        if amount <= 0:
            raise ValueError("Le montant doit être positif.")
        self.amounts.append(amount)

    def __len__(self):
        """Retourne le nombre d'articles dans la facture."""
        return len(self.amounts)

    def __str__(self):
        """Retourne une représentation textuelle de la facture."""
        total = sum(self.amounts)
        return f"Facture n°{self.invoice_id} – Articles : {len(self)} – Total : {total:.2f} €"
