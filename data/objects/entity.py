"""<Module "Simple RPG/game/objects/entity.py">
Description:
Contains the class for Entity() objects.
"""
# IMPORTS
#import [Module/Package]


class Entity(object):
    #? Constructor
    def __init__(self, _name: str,
                 _health: int,
                 _attack: int,
                 _defense: int,
                 _speed: int):
        """<Method "Simple RPG/data/objects/entity.Entity.__init__()">
        Description:
        Constructs the combatant, setting its attributes & properties to the provided values.
        Args:
            _name (String) : [description]
            _health (Integer) : [description]
            _attack (Integer) : [description]
            _defense (Integer) : [description]
            _speed (Integer) : [description]
        """
        #TODO: Set self.stat_points & self.turn_timer to the values of their respective keys within **modifiers
        self._name = _name
        self._health = _health
        self.attack = _attack
        self.defense = _defense
        self.speed = _speed
    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, value: int):
        if value <= 0:
            self._health = 0
        else:
            self._health = value
    @health.deleter
    def health(self):
        self._health = 0
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value: str):
        try:
            if not isinstance(value, str):
                raise TypeError("The name provided was not a string.")
            else:
                self._name = value
        except TypeError as e:
            print(e)
    @name.deleter
    def health(self):
        self._name = 0
        

# MAIN METHOD
def main():
    """<Method "Simple RPG/data/objects/entity.main()">
    Description:
    This is the main function of the script, called when the module is ran directly.
    """
    pass

# DRIVER CODE
if __name__ == "__main__":
    main()
    input("Press Enter To Exit.") #? This is added to keep the script from exiting after the logic is ran.
else:
    print(f"{__name__} was successfully imported.")
    