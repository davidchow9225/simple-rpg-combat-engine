"""<Module "Simple RPG/game/objects/player.py">
Description:
Contains the class for Player() objects.
"""
# IMPORTS
#import [Module/Package]


class Player(object):
    #? Constructor
    def __init__(self, _name: str,
                 _health: int,
                 _attack: int,
                 _defense: int,
                 _speed: int):
        """<Method "Simple RPG/data/objects/player.Player.__init__()">
        Description:
        Constructs the combatant, setting its attributes & properties to the provided values.
        Args:
            _name (String) : [description]
            _health (Integer) : [description]
            _attack (Integer) : [description]
            _defense (Integer) : [description]
            _speed (Integer) : [description]
        """
        super().__init__(_name, _health, _attack, _defense, _speed)
    #TODO: Add Interface Methods


# MAIN METHOD
def main():
    """<Method "Simple RPG/data/objects/player.main()">
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
    