from menus import Opening, Attack, CharSelection, Selection
from characters import Obi, Anakin, Kit, Mace, Stormtrooper
from battleOfGeonosis import Geonosis


selection = Opening()
character = Selection()
battle = Geonosis(character)
# attackSelection = Attack(battle)

attackSelection = battle.menus["Attack"](battle)
