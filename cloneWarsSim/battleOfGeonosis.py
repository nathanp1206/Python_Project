from menus import Attacks

class Geonosis():
    def __init__(self, character):
        # Attacks1()
        self.character = character
        self.menus = {
            "Attacks":Attacks
        }