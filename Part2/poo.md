# **Chapitre 2 – Programmation orientée objet en Python**

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

**Sortie attendue :**

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

> Les méthodes spéciales (dites *“dunder”*) rendent les objets **plus expressifs et intégrés au langage**.

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
>
> * un identifiant et une liste de montants,
> * `__len__()` → nombre d'articles,
> * `__str__()` → affichage formaté du total.

---

## TP 

Récupérez le TP à l’adresse suivante et faites-le par équipes de deux maximum.

[crypto](./TP_crypto.md)

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

**Utilisation :**

```python
u1 = User("Alice", "a@ex.com")
u2 = ManagerUser("Bob", "b@ex.com", 5)

print(u1.info(), ":", u1.permissions())
print(u2.info(), ":", u2.permissions())
```

**Sortie :**

```
Alice (a@ex.com) : ['read']
Bob (b@ex.com) : ['read', 'approve']
```

---

### **Exercice 3 – Héritage avec `super()` (version simplifiée)**

> Créez deux classes :
>
> * `Vehicle` : contient un attribut `brand` et une méthode `describe()` qui affiche `"Vehicle brand: <brand>"`.
> * `Car` : hérite de `Vehicle`, ajoute un attribut `model`, et redéfinit `describe()` en appelant `super().describe()` puis en affichant aussi le modèle.

---

## **4. Polymorphisme**

> Le **polymorphisme** permet d'utiliser **différentes classes de la même façon**,
> du moment qu'elles offrent **la même méthode**.
>
> En Python, on parle de **duck typing** :
> “si un objet sait faire ce qu'on lui demande, peu importe sa classe.”

---

### **Exemple simple**

```python
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

def make_it_speak(animal):
    animal.speak()
```

**Utilisation :**

```python
dog = Dog()
cat = Cat()

make_it_speak(dog)
make_it_speak(cat)
```

**Sortie :**

```
Woof!
Meow!
```

---

### **Exercice 4 – Polymorphisme**

> Créez deux classes :
>
> * `Car` avec une méthode `start()` affichant `"The car engine starts."`
> * `Bicycle` avec une méthode `start()` affichant `"You start pedaling."`
>
> Puis écrivez une fonction `start_vehicle(vehicle)` qui appelle `vehicle.start()`.
> Testez la fonction avec une voiture et un vélo.

---

## **5. Encapsulation et cohérence interne**

> L'encapsulation permet de **protéger les données internes** et de **maintenir la cohérence métier**.
> Python ne possède pas de vrais attributs privés, mais on peut utiliser :
>
> * la **convention** `_attribut` ou `__attribut`,
> * le **décorateur `@property`** pour contrôler lecture et écriture.

---

### **Exemple : validation automatique**

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

## **6. TP – Gestion de commandes**

> Objectif : modéliser un petit système de commandes en ligne.
> (Encapsulation facultative)

1. **`Product`**

   * Attributs : `name`, `price`
   * Méthode `__str__()` : affiche le nom et le prix

2. **`Customer`**

   * Attributs : `name`, `email`
   * Méthode `__str__()` : affiche les informations du client

3. **`Order`**

   * Attributs : `reference`, `customer`, `products` (liste vide)
   * Méthodes :

     * `add_product(product)`
     * `total()`
     * `__str__()`

---

### **Exemple attendu**

```python
p1 = Product("Keyboard", 45)
p2 = Product("Mouse", 25)

c1 = Customer("Alice", "alice@example.com")

order = Order("CMD001", c1)
order.add_product(p1)
order.add_product(p2)

print(order)
```

**Sortie attendue :**

```
Order CMD001
Customer: Alice (alice@example.com)
Items: 2 - Total: 70€
```
