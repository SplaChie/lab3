from heroes import Hero

class InventoryDecorator(Hero):
    def __init__(self, hero):
        self.hero = hero

    def get_description(self):
        return self.hero.get_description()

class ArmorDecorator(InventoryDecorator):
    def get_description(self):
        return f"{self.hero.get_description()} with Armor"

class WeaponDecorator(InventoryDecorator):
    def get_description(self):
        return f"{self.hero.get_description()} with Weapon"

class ArtifactDecorator(InventoryDecorator):
    def get_description(self):
        return f"{self.hero.get_description()} with Artifact"
