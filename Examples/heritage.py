# Another example
class Vehicle:
    def move(self):
        return "I am moving."

class Bicycle(Vehicle):
    def move(self):
        # We keep the original message + extend it
        return super().move() + " By pedaling!"

class Car(Vehicle):
    def move(self):
        # Extend behavior
        return super().move() + " By driving!"


# A fantasy example
class Wizard:
    def cast_spell(self):
        return "A mysterious spell occurs..."

class FireWizard(Wizard):
    def cast_spell(self):
        return super().cast_spell() + " *FLAMES everywhere*"

class IceWizard(Wizard):
    def cast_spell(self):
        return super().cast_spell() + " *Everything freezes*"