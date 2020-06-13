from menus import Attack

class Geonosis():
    def __init__(self, character):
        # Attacks1()
        self.character = character
        self.menus = {
            "Attack":Attack
        }