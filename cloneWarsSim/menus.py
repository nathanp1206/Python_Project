class Opening():
    def __init__(self):
        self.battles = {'Arantara', 'Christophsis', 'Corvair Sector', 'Geonosis', 'Murkhana', 'Teth'}

        self.count = 1
        for self.battle in self.battles:
            print("%s. %s" % (self.count, self.battle))
            self.count += 1
  
        self.openingSelection = input("Pick a battle to start(Type the number):\n")


class CharSelection():
    def __init__(self):
        self.character = {
            'Anakin Skywalker',
            'Obi-Wan Kenobi',
            'Mace Windu',
            'Kit Fisto',
            'StormTrooper'
        }
        self.count = 1
        for self.characters in self.character:
            print("%s. %s" % (self.count, self.characters))
            self.count += 1
    
        self.characterSelection = input("Pick a Character(Type the number):\n")

class Attacks():
    def __init__(self):
        from classes import DC15
        from classes import DC15X
        from classes import DC17M
        from classes import Lightsaber
        from characters import Dooku, Stormtrooper, Droids, Mace, Kit, Obi, Anakin

        self.attacks1 = []
        if self.weaponType == DC15 or weaponType == DC15X or weaponType == DC17M:
            self.attackChoices = [
                'Shoot',
                'Dodge'
            ]
            self.attacks1.append(self.attackChoices)
        elif Lightsaber:
            self.attackChoices = [
            'Chop',
            'Block',
            'Slash',
            'Lunge',
            'Dodge',
            ]
            self.attacks1.append(self.attackChoices)
        self.count = 1
        for self.attack in self.attacks1:
            print("%s. %s" % (self.count, self.attack))
            self.count += 1
        self.attackSelection = input("Pick an Attack(Type the number):\n")

