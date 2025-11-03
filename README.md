# **1. Vérifier l'installation de Python**

Ouvrir un terminal (ou PowerShell sur Windows), puis taper :

```bash
python --version
```

ou parfois :

```bash
python3 --version
```

Vous devez voir une version (par exemple `Python 3.11.6`).

> Si Python n'est pas installé :
>
> * **Windows** : télécharger depuis [python.org/downloads](https://www.python.org/downloads/) et cocher **“Add Python to PATH”** à l'installation.
> * **macOS/Linux** : Python est souvent déjà présent, sinon installez-le via `brew install python` (macOS) ou `sudo apt install python3` (Linux).

---

# **2. Créer un environnement virtuel**

Placez-vous dans votre dossier de projet (exemple : `C:\Users\user\projects\python_course` ou `~/Documents/python_course`).

Puis créez l'environnement virtuel :

```bash
python -m venv venv
```

Ici :

* `python -m venv` : lance le module de création d'environnements virtuels ;
* `venv` : nom du dossier qui contiendra l'environnement (vous pouvez le nommer `.venv` ou `env` si vous préférez).

> Ce dossier contiendra sa propre version de Python et de `pip`, séparée du reste du système.

---

# **3. Activer l'environnement virtuel**

### **Sous Windows (PowerShell ou CMD)**

```bash
venv\Scripts\activate
```

### **Sous macOS / Linux**

```bash
source venv/bin/activate
```

> Si tout va bien, vous verrez votre terminal afficher quelque chose comme :
>
> ```
> (venv) C:\Users\user\projects\python_course>
> ```

Cela signifie que l'environnement virtuel est **actif**.

---

# **4. Installer des bibliothèques dans l'environnement**

Quand l'environnement est actif, vous pouvez installer des modules sans affecter le reste du système :

```bash
pip install jupyter lab notebook
```

Vous pouvez aussi vérifier les paquets installés :

```bash
pip list
```

Et sauvegarder la liste pour la partager :

```bash
pip freeze > requirements.txt
```

---

# **5. Désactiver l'environnement**

Quand vous avez fini de travailler :

```bash
deactivate
```

Votre terminal redevient normal (le préfixe `(venv)` disparaît).

---

# **6. Reprendre le travail plus tard**

Quand vous revenez dans le dossier du projet :

* l'environnement virtuel existe toujours (`venv/`),
* il suffit de le **réactiver** :

```bash
source venv/bin/activate    # macOS / Linux
```

ou

```bash
venv\Scripts\activate       # Windows
```

---

# **7. (Optionnel) Recréer un environnement depuis un projet**

Si un autre développeur vous fournit un fichier `requirements.txt` :

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

# **Structure typique d'un projet Python**

```
python_course/
│
├── venv/                # environnement virtuel
├── data/                # données brutes ou nettoyées
├── src/                 # code source du projet
│   └── main.py
├── requirements.txt     # dépendances du projet
└── README.md
```


### Pour le déployer le cours 


## Pratique pour le déploiement du cours 

```bash
for f in *.html; do pandoc "$f" -o "pdf/${f%.html}.pdf" --pdf-engine=weasyprint; done

for f in *.md; do pandoc "$f" -o "pdf/${f%.md}.pdf" --pdf-engine=xelatex --standalone; done

for file in Slides/*.md; do
  marp "$file" --html --allow-local-files -o "docs/$(basename "${file%.md}.html")"
done

```

### Pour créer des slides 

En haut de chaque `markdown`

```md
---
marp: true
theme: default
paginate: true
class: lead
---
```
