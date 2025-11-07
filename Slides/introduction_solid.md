---
marp: true
theme: default
paginate: true
class: lead
---


# **Chapitre 3 – Introduction à SOLID : la responsabilité unique**


[Home](./index.html)

---

## **1. Pourquoi parler de SOLID ?**

Quand le code devient plus grand, il devient aussi plus fragile.
On ajoute une fonctionnalité, et ailleurs, quelque chose se casse.
Les classes grossissent, tout devient dépendant de tout.

Les principes **SOLID** ont été proposés pour rendre le code **plus clair, plus stable et plus facile à faire évoluer**.
Ils décrivent des **bonnes pratiques de conception orientée objet** qui favorisent la maintenance à long terme.

---

**SOLID**, c'est un acronyme pour :

* **S** – *Single Responsibility Principle*
* **O** – *Open/Closed Principle*
* **L** – *Liskov Substitution Principle*
* **I** – *Interface Segregation Principle*
* **D** – *Dependency Inversion Principle*

Mais pour commencer, on va se concentrer uniquement sur le **S** :

> Une classe ne doit avoir **qu'une seule responsabilité**,
> c'est-à-dire **une seule raison de changer**.

---

## **2. Comprendre le principe de responsabilité unique**

Quand une classe fait trop de choses, elle devient difficile à modifier et à tester.
Si tu dois la changer pour une raison, tu risques d'en casser une autre.

---

### **Exemple : une classe trop chargée**

```python
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate(self):
        return f"# {self.title}\n\n{self.content}"

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.generate())
        print("Report saved.")
```

`generate()` gère **le contenu du rapport** (métier)
`save_to_file()` gère **la sauvegarde** (persistance)

Deux responsabilités différentes sont dans la même classe.

---

### **Version corrigée (SRP appliqué)**

```python
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate(self):
        return f"# {self.title}\n\n{self.content}"


class FileSaver:
    def save(self, text, filename):
        with open(filename, "w") as f:
            f.write(text)
        print(f"{filename} saved.")
```

---

Usage des classes SPR

```python
report = Report("Weekly Report", "Everything is working fine.")
text = report.generate()

saver = FileSaver()
saver.save(text, "report.txt")
```

On a maintenant deux classes, chacune avec **une seule responsabilité** :

`Report` : crée le texte du rapport
`FileSaver` : gère la sauvegarde

