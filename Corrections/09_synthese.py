class Car:
    # le constructeur définir les variables de la classe
    def __init__(self, color, speed):
        self.color = color # valeurs partagée dans la classe
        self.speed = speed
        
    # fonction de la classe 
    def description(self):
        return f"une description de ma voiture coleur: {self.color}, vitesse: {self.speed} "

    # comment changer la couleur de la voiture avec une fonction de classe
    def change_color(self, newColor):
        self.color = newColor

    # methode qui change la vitesse
    def change_speed(self, speed):
        self.speed = speed 


# CREATION DE L'OBJET
# self == une création d'objet 
car1 = Car("red", 100) # self propre car1
print(car1.description())  # red
car1.change_color("vert") # changer la couleur 
car1.change_speed(200)
print(car1.description())  # vert


class Product:
    def __init__(self, price, name):
        self.name = name
        self.price = price

    #def description(self):
    #   return f"produit: {self.name} price: {self.price}"

    def setPrice(self, price):
        self.price = price 

    def setName(self, name):
        self.name = name

    # une méthode automatique qui est appelée quand on fait un print sur l'objet
    def __str__(self):
        return f"produit: {self.name} price: {self.price}"


apple = Product(0.8, "apple")
print(apple)