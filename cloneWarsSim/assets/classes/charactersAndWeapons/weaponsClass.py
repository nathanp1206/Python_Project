from jediClass import Jedi
from droidClass import Droid
from cloneClass import Clone

class Lightsaber():
    def __init__(self):
        self.classType = "Melee"
        self.chop = 60
        self.block = 0
        self.slash = 100
        self.lunge = 85
    


class Blaster():
    def __init__(self):
        self.classType = "Ranged"

class E5(Blaster):
    def __init__(self):
        self.shot = 60
        #Droids

class DC15(Blaster):
    def __init__(self):
        self.shot = 60
        #Republic Troopers

class DC15X(Blaster):
    def __init__(self):
        self.shot = 100
        #Sniper

class DC17M(Blaster):
    def __init__(self):
        self.shot = 70
        #Clone Commandos