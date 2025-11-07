---
marp: true
theme: default
paginate: true
class: lead
---

# **Chapitre 2 – Programmation orientée objet en Python**

[Home](./index.html)


---

## **1. De la modélisation au code**

> Une **classe** représente une **entité du domaine** (ex. : utilisateur, commande, facture…).
> Un **objet** représente une **instance concrète** de cette entité.

---

### **Exemple de modélisation**

**Cas : gestion d'utilisateurs dans une application.**

| Élément du modèle | Exemple concret                     |
| ----------------- | ----------------------------------- |
| Entité            | Utilisateur                         |
| Attributs         | nom, email, rôle                    |
| Comportements     | activer(), désactiver(), afficher() |

---

### **Implémentation simple**

```python
class User:
    def __init__(self, name, email, active=True):
        self.name = name
        self.email = email
        self.active = active

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True
```

---

**Utilisation :**

```python
u1 = User("Alice", "alice@example.com")
u2 = User("Bob", "bob@example.com", active=False)

u1.deactivate()
print(u1.active, u2.active)
```

---

### **Exercice 1 – Première modélisation**

> Modéliser une classe `Customer` avec les attributs `name`, `address`, `is_vip`.
> Ajouter une méthode `upgrade_to_vip()` et une méthode `show()` pour afficher son statut.

---

### **Exemple d'utilisation**

```python
c1 = Customer("Alice Martin", "12 rue du Parc, Lyon")
c2 = Customer("Bob Leroy", "5 avenue de la Gare, Nantes", is_vip=True)

c1.show()

print("\n--- Alice devient VIP ---")
c1.upgrade_to_vip()
c1.show()
```
```
Customer: Alice Martin
Address: 12 rue du Parc, Lyon
Status: Standard

--- Alice devient VIP ---
Customer: Alice Martin
Address: 12 rue du Parc, Lyon
Status: VIP
```

---

## **2. Méthodes spéciales et représentation**

> Les méthodes spéciales (dites *"dunder"*) rendent les objets **plus expressifs et intégrés au langage**.

---

### **Exemple : classe `Order`**

```python
class Order:
    def __init__(self, order_id, products):
        self.order_id = order_id
        self.products = products  # liste de Product

    def total(self):
        return sum(p.price for p in self.products)

    def __len__(self):
        return len(self.products)

    def __str__(self):
        return f"Order {self.order_id} – {len(self)} items – total {self.total():.2f}€"

    def __contains__(self, product_name):
        return any(p.name == product_name for p in self.products)
```

---

**Utilisation :**

```python
p1 = Product("Mouse", 25)
p2 = Product("Keyboard", 45)
order = Order("A123", [p1, p2])
print(order)
print("Mouse" in order)
```

---

### **Exercice 2 – Représentation**

> Créer une classe `Invoice` avec :
> un identifiant et une liste de montants,
> `__len__()` → nombre d'articles,
> `__str__()` → affichage formaté du total.

---

## TP Crypto 

Récupérez le TP à l'adresse suivante et faites-le par équipes de deux maximum.

[crypto](https://antoine07.github.io/python_expert/TP_crypto.html)

---

## Exercice Bank

Simuler un dépôt d'argent sur un compte à travers une classe Bank qui appelle une méthode de Account.

---

---

## Exercice Panier & Boutique

Simuler l'ajout d'un article dans un panier à travers une classe Shop qui appelle une méthode de Cart.

---

## 1. Bilan point sur la pratique des exceptions 1/2

```python
# Dans la classe
def withdraw(self, amount):
    if amount > self.balance:
        raise ValueError("Solde insuffisant")
    self.balance -= amount

# À l'extérieur (ex : simulation)
try:
    account.withdraw(500)
except ValueError as e:
    print("Erreur :", e)
```

---

## 2. Bilan sur le couplage

```python
class Shop:
    def __init__(self):
        self.cart = Cart()   # ← création interne → couplage fort

class Shop:
    def __init__(self, cart):
        self.cart = cart

cart = Cart()
shop = Shop(cart)
```

---

### Couplage faible

Une classe ne doit pas connaître les détails internes d'une autre classe.

**Mauvais** :

shop.cart.items["banane"] = 3    # Accès interne direct


**Bon** :

shop.cart.add_product(banane, 3) # On passe par la méthode de la classe


On utilise les méthodes, pas les attributs internes, c'est mieux.

---

## **Refactorisation – Rappel synthétique (1 slide)**

**Objectif** : rendre le code plus clair, maintenable et extensible.
**Principe** : modifier l'**organisation** du code sans changer le **comportement**.
**Bonnes pratiques** :

Extraire des méthodes trop longues → **fonctions plus petites et lisibles**
Éviter **duplication** → centraliser la logique partagée
Renommer pour **clarifier l'intention** (variables, méthodes, classes)
**Injecter** les dépendances → éviter couplage fort
Laisser les classes **lever** des exceptions, gérer les erreurs **à l'extérieur**
**Résultat attendu** : code plus simple, stable, testable, évolutif.

---

## **3. Héritage et spécialisation**

> L'héritage permet de **réutiliser**, **étendre** et **spécialiser** des comportements communs entre plusieurs classes.
> La fonction `super()` permet d'appeler le comportement de la classe parente pour **éviter la duplication** et **ajouter seulement les différences**.

---

### **Exemple : utilisateurs avec rôles**

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def permissions(self):
        return ["read"]

    def info(self):
        return f"{self.name} ({self.email})"
```

---

#### Spécialisation sans `super()`

```python
class AdminUser(User):
    def permissions(self):
        # On écrase complètement la méthode du parent
        return ["create", "delete", "update", "read"]
```

Cela fonctionne, mais on **perd** les permissions héritées du parent.
Si la classe `User` évolue, `AdminUser` n'en bénéficiera pas.

---

#### Spécialisation avec `super()`

```python
class ManagerUser(User):
    def __init__(self, name, email, team_size):
        super().__init__(name, email)  # Appel du constructeur parent
        self.team_size = team_size

    def permissions(self):
        base_permissions = super().permissions()
        return base_permissions + ["approve"]
```

---

**Utilisation :**

```python
u1 = User("Alice", "a@ex.com")
u2 = ManagerUser("Bob", "b@ex.com", 5)

print(u1.info(), ":", u1.permissions())
print(u2.info(), ":", u2.permissions())
```
```
Alice (a@ex.com) : ['read']
Bob (b@ex.com) : ['read', 'approve']
```

---

### **Exercice – Héritage avec `super()`**

> Créez deux classes :
> `Vehicle` : contient un attribut `brand` et une méthode `describe()` qui affiche `"Vehicle brand: Renault"`.
> `Car` : hérite de `Vehicle`, ajoute un attribut `model`, et redéfinit `describe()` en appelant `super().describe()` puis en affichant aussi le modèle.

---

### Exercice – Produits, Livres et Panier (POO)

Créer une classe `Product` avec `name` et `price_ht`, ainsi qu'un attribut de classe `VAT` (ex. 0.20). La méthode `price_ttc()` calcule le prix TTC.

Créer une classe `Book` qui hérite de `Product`, ajoute `author`, possède son propre taux de TVA (attribut de classe `VAT` différent) et redéfinit `price_ttc()`. Utiliser `super()` dans le constructeur.

Créer une classe `Cart` contenant une liste `items`. Elle doit permettre `buy(product)`, `restore(product)`, `reset()` et `total()` qui renvoie le total TTC du panier. Le panier ne doit pas créer de produits, seulement recevoir ceux créés à l'extérieur.

Dans le programme principal : créer au moins deux `Product` et deux `Book`, les ajouter au panier, afficher le total, modifier les valeurs de `Product.VAT` ou `Book.VAT`, puis afficher à nouveau le total pour observer l'effet.


---

## **5. Encapsulation et cohérence interne**

> L'encapsulation permet de **protéger les données internes** et de **maintenir la cohérence métier**.
> Python ne possède pas de vrais attributs privés, mais on peut utiliser :
>
> la **convention** `_attribut` ou `__attribut`,
> le **décorateur `@property`** pour contrôler lecture et écriture.

---

### **Exemple : validation setter getter**

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty")
        self.__name = value
```

**Utilisation :**

```python
p = Product("Laptop", 700)
print(p.name)
p.price = -10  # déclenche une erreur
```

---

### **Exercice 5 – Encapsulation**

> Créer une classe `Account` avec un solde (`_balance`).
>
> * Utiliser `@property` pour lire/écrire ce solde.
> * Interdire les dépôts ou retraits négatifs.
> * Ajouter `deposit()` et `withdraw()`.

---

### **Polymorphisme : définition**

Le polymorphisme est la capacité pour plusieurs objets différents de répondre à une même méthode, mais chacun à sa manière.
On s'adresse à l'objet **par son comportement**, pas par son type.
Autrement dit : *« On sait que l'objet sait faire, mais pas comment il le fait. »*
Cela permet d'écrire du code plus **générique**, **réutilisable** et **extensible**, sans conditions du type `if type == ...`.

---

### **Exemple**

```python
class Product:
    def price_ttc(self):
        return self.price_ht * (1 + Product.VAT)

class Book(Product):
    def price_ttc(self):
        return self.price_ht * (1 + Book.VAT)

class Cart:
    def total(self):
        return sum(item.price_ttc() for item in self.items)
```

Ici `Cart` appelle `price_ttc()` sans connaître le type précis de l'objet.
Si l'objet est un `Product` ou un `Book`, la méthode exécutée sera celle correspondante.
C'est **le même appel**, mais **un comportement adapté** selon l'objet.

---

### **Intérêt**

Permet d'ajouter de nouveaux types d'objets **sans modifier le code existant**.
Le polymorphisme évite les tests de type, les duplications et les dépendances inutiles.
Il rend le système plus souple : le code s'appuie sur **ce que l'objet sait faire**, pas sur **ce qu'il est**.
C'est un principe majeur pour obtenir un code **maintenable**, **propre**, et **ouvert à l'évolution**.

---

### **Lien entre héritage et polymorphisme**

L'héritage permet de **définir un comportement commun** dans une classe parent (ex : `Product`) et de le **spécialiser** dans les classes enfants (ex : `Book`).
Le polymorphisme utilise cet héritage pour permettre **un même appel de méthode** à produire **différents comportements** selon l'objet.

---

### Exemple 1/2

```python
class Product:
    def price_ttc(self):
        return self.price_ht * (1 + Product.VAT)

class Book(Product):           # Héritage
    def price_ttc(self):       # Polymorphisme (surcharge)
        return self.price_ht * (1 + Book.VAT)
```

---

### Exemple 2/2

Quand le panier appelle :

```python
for item in cart.items:
    total += item.price_ttc()
```

Il **ne sait pas** s'il a un `Product` ou un `Book`.
Mais **il sait** que chaque objet possède `price_ttc()`.

**Héritage = structure commune.**
**Polymorphisme = comportements adaptés.**
