# **Chapitre 1 – Expressivité et idiomes Python**

---

## **1. Style et culture Python**

---

### **1.1 Le style PEP8**

Le guide officiel **PEP8** décrit la manière d'écrire un code Python lisible.
Python ne se limite pas à "faire fonctionner le code" : il s'agit de **le rendre clair pour les autres**.

Il existe une liste complète de règles, mais nous introduisons ici les plus importantes pour la suite du cours.
→ [Documentation officielle PEP 8](https://peps.python.org/pep-0008/)

**Principes essentiels :**

* **Indentation** : 4 espaces (pas de tabulations — la touche *Tab* dans vos éditeurs insère généralement 4 espaces)
* **Noms** :

  * variables et fonctions → `snake_case`
  * classes → `PascalCase`
* **Espaces** : autour des opérateurs et après les virgules.
* **Lisibilité** : une ligne = une action.

**Exemple :**

```python
def compute_total(prices):
    total = sum(prices)
    return total
```

---

### **1.2 Le Zen of Python**

À lire une fois dans le terminal :

```python
import this
```

> Beautiful is better than ugly.
> Simple is better than complex.
> Readability counts.

**Idée principale :**

> Écrire du code **pour être lu et compris** avant d'être exécuté.

---

### **Exercice 1 – Rendre le code lisible**

> Corrigez ce code pour qu'il respecte la PEP8 et soit clair par rapport aux règles énoncées dans ce cours.

```python
def addNumbers(a,b):return(a+b)
nums=[1,2,3]
for n in nums:print(addNumbers(n,n))
```

---

## **2. Écrire de manière expressive**

---

### **2.1 Compréhensions de liste**

Une **compréhension** permet de transformer ou filtrer une séquence en une seule ligne lisible.

```python
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
evens = [n for n in numbers if n % 2 == 0]
```

Ces deux exemples remplacent des boucles plus longues et restent compréhensibles.

**Exercice 2 – Filtrage simple**

> À partir de la liste `notes = [10, 15, 8, 18, 13]`, créez :
>
> * une liste des notes >= 12,
> * une liste des notes doublées.

---

### **2.2 Compréhensions de dictionnaires et ensembles**

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
students = {name: score for name, score in zip(names, scores)}
passed = {name for name, score in students.items() if score >= 80}
```

**Exercice 3 – Construction de dictionnaire**

> Construisez un dictionnaire `lengths` associant chaque fruit de `["apple", "banana", "pear"]` à sa longueur.
> Puis créez un ensemble `long_words` des fruits de plus de 5 lettres.

---

### **2.3 Fonctions natives idiomatiques**

Python fournit de nombreuses fonctions prêtes à l'emploi :

```python
numbers = [3, 6, 9, 12, 15]
total = sum(numbers)
maximum = max(numbers)
evens = list(filter(lambda x: x % 2 == 0, numbers))
doubles = list(map(lambda x: x * 2, numbers))
```

**Exercice 4 – Trois approches**

> Calculez la somme des nombres impairs entre 1 et 10 :
>
> 1. avec une boucle `for`
> 2. avec une compréhension
> 3. avec `filter` et `sum`

---

## **3. Lecture et écriture de fichiers**

---

### **3.1 Lecture simple**

```python
with open("data.txt", "r") as f:
    content = f.read()
print(content)
```

Le mot-clé `with` garantit la **fermeture automatique du fichier**, même si une erreur se produit.

---

### **3.2 Lecture ligne à ligne**

```python
with open("data.txt") as f:
    for line in f:
        print(line.strip())
```

**Exercice 5 – Comptage de lignes**

> Créez un fichier `words.txt` contenant une dizaine de mots.
> Écrivez un programme qui affiche :
>
> * le nombre total de lignes,
> * le mot le plus long.

---

### **3.3 Écriture dans un fichier**

```python
data = ["apple", "banana", "pear"]

with open("fruits.txt", "w") as f:
    for fruit in data:
        f.write(f"{fruit}\n")
```

Le mode `"w"` **remplace** le contenu du fichier.
Le mode `"a"` **ajoute** à la suite.

**Exercice 6 – Enregistrement de résultats**

> Demandez à l'utilisateur 3 prénoms et enregistrez-les dans un fichier `names.txt`.

---

## **4. Lire des données et vérifier leur validité**

---

### **4.1 Nettoyage de données simples**

Quand on lit un fichier, certaines lignes peuvent être vides ou non numériques.
Avant d'apprendre les *exceptions*, on peut les filtrer avec des **conditions simples** :

```python
temperatures = ["12.3", "", "abc", "15.0", "13.2"]

cleaned = []
for t in temperatures:
    if t.strip() == "":
        continue
    if t.replace(".", "", 1).isdigit():
        cleaned.append(float(t))

print(cleaned)
```

---

### **Exercice 7 – Nettoyage basique**

> Écrivez une fonction `clean_numbers(lines)` qui :
>
> * prend une liste de chaînes (ex : valeurs lues dans un fichier),
> * ignore les lignes vides ou non numériques,
> * renvoie une liste de `float`.

**Indice :**

> utilisez `str.isdigit()` ou la vérification sur `replace(".", "", 1)`.

---

### **4.2 Petits calculs sur des données**

Une fois la liste propre, on peut utiliser les idiomes Python pour l'analyse :

```python
values = [12.3, 14.1, 15.8, 13.0]
avg = sum(values) / len(values)
min_val, max_val = min(values), max(values)
```

**Exercice 8 – Analyse express**

> À partir d'une liste `heights = [170, 180, 165, 190]`, affichez :
>
> * la moyenne,
> * la taille la plus petite et la plus grande,
> * le nombre de personnes au-dessus de la moyenne.

---

## **5. Introduction pratique : erreurs et vérifications**

---

Avant d'aborder les *exceptions* (chapitre suivant), il faut comprendre **pourquoi elles existent**.

Certaines opérations échouent naturellement :

* ouverture d’un fichier manquant,
* conversion d’un texte en nombre.

```python
x = float("abc")  # ValueError
with open("missing.txt") as f:  # FileNotFoundError
    pass
```

---

### **Prévenir sans exceptions**

On peut parfois anticiper **avec des conditions simples** :

```python
text = "12.5"
if text.replace(".", "", 1).isdigit():
    value = float(text)
else:
    print("Invalid number")
```

---

### **Exercice 9 – Lecture sûre**

> Écrivez une fonction `read_numbers(filename)` qui :
>
> * lit un fichier contenant un nombre par ligne,
> * ignore les lignes vides ou non valides,
> * renvoie une liste de nombres valides.

---

# **Chapitre 3 – Gestion des erreurs avec `try / except`**

---

## 🎯 **Objectif**

Rendre un programme **robuste** : ne pas planter quand une erreur survient, mais réagir proprement
(message clair, valeur par défaut ou poursuite du code).

---

## **1. Qu’est-ce qu’une exception ?**

Une *exception* est une **erreur détectée par Python** pendant l’exécution.

Exemple :

```python
x = int("abc")
```

Résultat :

```
ValueError: invalid literal for int() with base 10: 'abc'
```

---

## **2. Gérer une erreur avec `try / except`**

```python
try:
    x = int(input("Entrez un nombre : "))
    print("Carré :", x**2)
except ValueError:
    print("Ce n'est pas un nombre valide.")
```

👉 Si l’utilisateur entre `"abc"`, l’erreur est interceptée et le programme continue.

**Exercice 1 – Conversion sûre**

> Demandez un nombre à l’utilisateur et affichez son carré.
> Si la saisie est invalide, affichez un message.

---

## **3. Plusieurs types d’erreurs**

```python
try:
    f = open("data.txt")
    content = f.read()
    print(int(content))
except FileNotFoundError:
    print("Le fichier est introuvable.")
except ValueError:
    print("Le contenu n'est pas un nombre.")
```

**Exercice 2 – Lecture protégée**

> Essayez d’ouvrir un fichier inexistant, puis corrigez votre code avec un bloc `try/except`.

---

## **4. Application : nettoyage de données**

Cas fréquent : une liste contient des valeurs invalides.

```python
data = ["12.3", "abc", "15.0", ""]

cleaned = []
for d in data:
    try:
        cleaned.append(float(d))
    except ValueError:
        print("⚠️ Ignoré :", d)

print(cleaned)
```

**Exercice 3 – Nettoyage**

> Reprenez ce code et ajoutez un **compteur** du nombre de valeurs invalides rencontrées.

---

## **5. Lecture sécurisée d’un fichier**

```python
def read_numbers(filename):
    values = []
    try:
        with open(filename) as f:
            for line in f:
                try:
                    values.append(float(line.strip()))
                except ValueError:
                    print("Ligne ignorée :", line.strip())
    except FileNotFoundError:
        print("Fichier introuvable :", filename)
    return values
```

**Exercice 4 – Fichier et erreurs**

> Créez un fichier `data.txt` contenant des valeurs et quelques erreurs.
> Testez `read_numbers("data.txt")` et observez le comportement.

---

## **6. Bilan**

| Objectif                          | Exemple                    |
| --------------------------------- | -------------------------- |
| **Empêcher un crash**             | `try / except`             |
| **Spécifier le type d’erreur**    | `except ValueError:`       |
| **Ignorer une erreur ponctuelle** | `continue` dans une boucle |
| **Informer l’utilisateur**        | `print("Erreur : ...")`    |

---

## **7. Préparation du TP – Analyse de températures de janvier**

---

Objectif du TP : combiner tout ce qui a été appris.

1. Lire un fichier `temperatures_january.txt` (31 jours).
2. Nettoyer les valeurs incorrectes.
3. Calculer :

   * la moyenne, le min et le max,
   * le nombre de jours sous 0°C,
   * le nombre de jours au-dessus de la moyenne.
4. Produire un résumé à l'écran puis dans un fichier texte.

Ce TP mobilisera :

* **fichiers**
* **listes et compréhensions**
* **calculs expressifs**
* **try / except** pour gérer les erreurs de données

