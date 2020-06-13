from menus import Attack
from characters import Dooku

class Geonosis():
    def __init__(self, character):
        # Attacks1()
        self.character = character
        self.menus = {
            "Attack":Attack
        }

def Damage(attackSelection):
    import random
    damageDone = None
    if attackSelection == '1':
        damageDone = 60 * random.randint(1,3)
        print('You did %s damage!' % damageDone)
    elif attackSelection == '2':
        damageDone = 0
        print('You successfully dodged')
    elif attackSelection == '3':
        damageDone = 100 * random.randint(1,3)
        print('You did %s damage!' % damageDone)
    elif attackSelection == '4':
        damageDone = 85 * random.randint(1,3)
        print('You did %s damage!' % damageDone)
    elif attackSelection == '5':
        damageDone = 0
        print('You successfully blocked')
    return damageDone

def Health(damageDone, healthLeft):
    healthRemoval = healthLeft - damageDone
    if healthRemoval > 0:
        print('Dooku has %s HP left' % healthRemoval)
    elif healthRemoval < 0:
        print('You killed Count Dooku!')
    healthLeft = healthRemoval
    return healthLeft

