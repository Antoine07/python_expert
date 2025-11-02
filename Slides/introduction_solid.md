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

* `Report` : crée le texte du rapport
* `FileSaver` : gère la sauvegarde

---

### **Exercice 1 – Classe trop lourde**

> La classe suivante fait trop de choses.
> Refactorise-la en deux classes séparées, chacune avec une seule responsabilité.

```python
class Logger:
    def __init__(self, filename):
        self.filename = filename

    def log_message(self, message):
        from datetime import datetime
        # formatage de l'heure
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        full_message = f"[{timestamp}] {message}"
        with open(self.filename, "a") as f:
            f.write(full_message + "\n")
        print(full_message)
```

Une partie gère la **mise en forme du message**.
L'autre gère **l'écriture dans un fichier**.

---

### **Exercice 2 – Validation et affichage**

> Crée une classe `User` avec `name`, `email`.
> Ajoute une validation dans une autre classe (`UserValidator`)
> et une classe `UserPrinter` pour afficher les infos.
>
> Chaque classe doit avoir **une seule raison de changer** :
>
> la structure de l'objet,
> la logique de validation,
> la manière d'afficher.

---

## **4. Conclusion**

Le **Single Responsibility Principle** est le fondement des autres principes SOLID.
En Python, il consiste à :

* donner à chaque classe **une seule responsabilité claire**,
* séparer la **logique métier** de la **présentation** ou de la **persistance**,
* réduire le couplage entre les parties du code.

Une fois ce principe acquis, les étudiants peuvent aborder :

* **O (Open/Closed)** pour apprendre à étendre sans modifier,
* puis plus tard, **L**, **I**, **D** pour des architectures plus souples.

---

## **TP – Application du SRP : gestion d'un panier d'achat**

---


Modéliser un panier (`Cart`) dans une boutique en ligne.
On veut ajouter, retirer des produits et calculer le total.
Mais on veut aussi pouvoir **afficher** et **sauvegarder** le panier.

---

### **Mauvaise version (violations du SRP)**

[Fichier de la classe](./Examples/BadCart.py)

La classe fait **trop de choses** :

gestion des données,
affichage,
sauvegarde.


---

## Merci de votre attention

[Home](./index.html)