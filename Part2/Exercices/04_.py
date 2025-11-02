class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def summary(self):
        """Retourne les 50 premiers caractères du contenu."""
        return self.content[:50] + ("..." if len(self.content) > 50 else "")

class Report(Document):
    def __init__(self, title, content, author):
        super().__init__(title, content)
        self.author = author

    def summary(self):
        """Résumé incluant l'auteur."""
        base_summary = super().summary()
        return f"[Rapport de {self.author}] {base_summary}"

class ConfidentialReport(Report):
    def summary(self):
        """Résumé masquant une partie du contenu."""
        base_summary = super().summary()
        hidden = base_summary[:30] + "..." + "[CONTENU CONFIDENTIEL]"
        return hidden
