# class Opening():
#     def __init__(self):
def Opening():
    battles = {'Geonosis'}
    count = 1
    for battle in battles:
        print("%s. %s" % (count, battle))
        count += 1
  
    openingSelection = input("Pick a battle to start(Type the number):\n")
    return openingSelection


class CharSelection():
    from characters import Anakin, Obi, Mace, Kit, Stormtrooper

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
        if self.characterSelection == '1':
            self.characterSelection = 'Anakin'
        elif self.characterSelection == '2':
            self.characterSelection = 'Obi'
        elif self.characterSelection == '3':
            self.characterSelection = 'Mace'
        elif self.characterSelection == '4':
            self.characterSelection = 'Kit'
        elif self.characterSelection == '5':
            self.characterSelection = 'StormTrooper'

def Attacks(battle):
    weaponType = battle.character.weaponType

    attacks1 = []
    if weaponType == "Ranged":
        attackChoices = [
            'Shoot',
            'Dodge'
        ]
        attacks1.append(attackChoices)
    elif weaponType == "Melee":
        attackChoices = [
        'Chop',
        'Block',
        'Slash',
        'Lunge',
        'Dodge',
        ]
        attacks1.append(attackChoices)
    count = 1
    for attack in attacks1:
        print("%s. %s" % (count, attack))
        count += 1
    attackSelection = input("Pick an Attack(Type the number):\n")
    return attackSelection