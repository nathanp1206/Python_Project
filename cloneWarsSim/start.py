from menus import Opening, Attacks, CharSelection
from characters import Obi
from battleOfGeonosis import Geonosis


selection = Opening()
character = CharSelection().characterSelection
print('You selected %s' % character)

battle = Geonosis(character)
attackSelection = Attacks(battle)
attackSelection = battle.menus["Attacks"](battle)
print(attackSelection)