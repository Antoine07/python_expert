#  Exercice — Mini-plateforme Crypto Orlab Exchange

## 🎯 Objectif

Créer un petit programme orienté objet en Python simulant une plateforme d'achat et de suivi de cryptomonnaies.

## Contraintes

- Utilisez PEP8
- L'objet
- Les fichiers 
- Les exceptions

---

##  Contexte

L'entreprise **Orlab Exchange** souhaite développer un prototype simplifié de sa plateforme d'investissement en cryptomonnaies.
Un utilisateur possède un solde en euros et peut acheter différentes cryptos (ex. : BTC, ETH).
Il doit être possible de :

* réaliser des achats de cryptos,
* consulter la valeur totale du portefeuille,
* afficher un rapport des avoirs,
* enregistrer les données dans un fichier.

---

## Spécifications fonctionnelles

1. **Solde et portefeuille**

   * Le portefeuille commence avec un solde de 1000 €.
   * Il doit contenir le montant détenu pour chaque crypto achetée.

2. **Achat**

   * L'utilisateur peut acheter une crypto donnée (par son symbole, son prix et la quantité).
   * Si le coût dépasse le solde disponible, l'achat est refusé.
   * Le solde en euros diminue du montant dépensé.

3. **Consultation**

   * Le programme doit permettre de connaître la valeur totale du portefeuille à partir d'un dictionnaire des prix actuels.
   * La valeur totale correspond au solde en euros + valeur de chaque crypto.

4. **Affichage**

   * Un rapport texte doit présenter :

     * les cryptos détenues et leurs valeurs actuelles,
     * le solde en euros,
     * la valeur totale du portefeuille.

5. **Sauvegarde**

   * Les informations du portefeuille doivent pouvoir être sauvegardées dans un fichier texte.

---

## Exemple d'utilisation attendue

```python
prices = {"BTC": 65000, "ETH": 3500}

# création d'un portefeuille
wallet = Wallet()

# exécution d'achats
trader = Trader(wallet)
trader.buy("BTC", prices["BTC"], 0.01)
trader.buy("ETH", prices["ETH"], 0.2)

# affichage d'un rapport
PortfolioReporter.print(wallet, prices)

# sauvegarde des données
WalletSaver.save(wallet)
```

---

##  Données de test

Utiliser le dictionnaire suivant pour simuler les prix du marché :

```python
prices = {"BTC": 65000, "ETH": 3500, "DOGE": 0.12}
```

---

## Attendus

* Un code structuré et clair.
* Des classes aux responsabilités bien délimitées : portefeuille, opérations d'achat, affichage, etc.
* Un comportement identique à celui de l'exemple d'utilisation.
