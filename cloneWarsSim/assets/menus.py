class Opening():
    battles = {'Arantara', 'Christophsis', 'Corvair Sector', 'Geonosis', 'Murkhana', 'Teth'}

    count = 1
    for battle in battles:
        print("%s. %s" % (count, battle))
        count += 1
  
    openingSelection = input("Pick a battle to start(Type the number):\n")


class CharSelection():
    character = {
        'Anakin Skywalker',
        'Obi-Wan Kenobi',
        'Mace Windu',
        'Kit Fisto',
        'StormTrooper'
    }
    count = 1
    for characters in character:
        print("%s. %s" % (count, characters))
        count += 1
    
    characterSelection = input("Pick a Character(Type the number):\n")

class Attack():

    from weapons import Weapons

    attacks = []
    if Weapons.Blaster:
        attackChoices = [
            'Shoot',
            'Dodge'
            ]
        attacks.append(attackChoices)
    elif Weapons.Lightsaber:
        attackChoices = [
        'Chop',
        'Block',
        'Slash',
        'Lunge',
        'Dodge',
        ]
        attacks.append(attackChoices)
    count = 1
    for attack in attacks:
        print("%s. %s" % (count, attack))
        count += 1
    attackSelection = input("Pick an Attack(Type the number):\n")
