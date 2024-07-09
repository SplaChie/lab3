class Hero:
    def __init__(self, name):
        self.name = name

    def get_description(self):
        return self.name

class Warrior(Hero):
    def get_description(self):
        return f"Warrior: {self.name}"

class Mage(Hero):
    def get_description(self):
        return f"Mage: {self.name}"

class Paladin(Hero):
    def get_description(self):
        return f"Paladin: {self.name}"
