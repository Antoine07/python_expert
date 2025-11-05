
class Car:
    def __init__(self, name, color, speed, phare):
        self.name = name
        self.color = color
        self.speed = speed
        self.phare = phare
        
    def __str__(self):
        return f"Color: {self.color} Speed: {self.speed} Phare: {self.phare.buld}"
    
class Phare:
    def __init__(self, buld):
        self.buld = buld     
    
phare_blue = Phare("Blue") # création d'un phare
twingo = Car("Twingo", "Red", 130, phare_blue)
print(twingo)