from classes import DarkSide
from classes import Lightsaber
from classes import Clone
from classes import DC15, DC15X, DC17M
from classes import Jedi
from classes import Droid


class Dooku(DarkSide):
    def __init__(self):
        self.lightsaberColor = "Red"

class Stormtrooper(Clone):
    def __init__(self):
        print("We're just clones, sir.")

class Droids(Droid):
    def __init__(self):
        print("Roger, roger.")

class Obi(Jedi):
    def __init__(self):
        self.lightsaberColor = "Blue"
        self.race = "Human"

class Mace(Jedi):
    def __init__(self):
        self.lightsaberColor = "Purple"
        self.race = "Korunnai"

class Kit(Jedi):
    def __init__(self):
        self.lightsaberColor = "Green"
        self.race = "Nautolan"

class Anakin(Jedi):
    def __init__(self):
        self.lightsaberColor = "Blue"
        self.race = "Human"