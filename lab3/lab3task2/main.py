from heroes import Warrior, Mage, Paladin
from decorators import ArmorDecorator, WeaponDecorator, ArtifactDecorator

def main():
    warrior = Warrior("Aragorn")
    mage = Mage("Gandalf")
    paladin = Paladin("Uther")

    warrior_with_armor = ArmorDecorator(warrior)
    mage_with_weapon = WeaponDecorator(mage)
    paladin_with_artifact = ArtifactDecorator(paladin)

    print(warrior_with_armor.get_description())
    print(mage_with_weapon.get_description())
    print(paladin_with_artifact.get_description())

    fully_equipped_warrior = ArtifactDecorator(WeaponDecorator(ArmorDecorator(warrior)))
    print(fully_equipped_warrior.get_description())

if __name__ == "__main__":
    main()
