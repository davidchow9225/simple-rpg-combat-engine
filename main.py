"""<Module "Simple RPG/main.py">
Description:
Main module for the Simple RPG combat engine.
"""
# IMPORTS
#import [Module/Package]
from data.objects import Game, Entity, Player  #TODO: Create modules containing classes for Entities & Players.


def character_creation(default: bool = False):
    """<Method "Simple RPG/main.character_creation()">
    Description:
    This is a debugging module method that fetches character data.
    Args:
            default (Boolean): Skips user input, returning default values instead.
    Returned Values:
        _name (String)
        _health (Integer)
        _attack (Integer)
        _defense (Integer)
        _speed (Integer)
    """
    if default:
        _name = "Placeholder Name"
        _health = 10
        _attack = 1
        _defense = 1
        _speed = 1
    else:
        _name = input("Please enter your character's name.\n")
        _health = input("Please enter your character's health.\n")
        _attack = input("Please enter your character's attack.\n")
        _defense = input("Please enter your character's defense.\n")
        _speed = input("Please enter your character's speed.\n")
    return _name, _health, _attack, _defense, _speed

#TODO: Create method that fetches Game() modifiers.
def game_modifiers(default: bool = False):
    """<Method "Simple RPG/main.character_creation()">
    Description:
    This is a debugging module method that fetches game instance modifiers.
    Args:
            default (Boolean): Skips user input, returning default values instead.
    Returned Values:
        _stat_points (Integer)
        _turn_seconds (Integer)
    """
    if default:
        _stat_points = 15
        _turn_duration = 300
    else:
        _stat_points = input("Please enter your character's name.\n")
        _turn_duration = input("Please enter your character's health.\n")
    return _stat_points, _turn_duration


# MAIN METHOD
def main():
    """<Method "Simple RPG/main.main()">
    Description:
    This is the main function of the script, called when the module is ran directly.
    """
    #* Define local variables
    _name_a, _health_a, _attack_a, _defense_a, _speed_a = character_creation()
    _name_b, _health_b, _attack_b, _defense_b, _speed_b = character_creation()
    _stat_points, _turn_duration = game_modifiers(True)
    #* Construct an instance of the Player Class from the first set of local variables.
    _combatant_a = Player(_name_a,
                          _health_a,
                          _attack_a,
                          _defense_a,
                          _speed_a)
    #* Construct an instance of the Entity Class from the second set of local variables.
    _combatant_b = Entity(_name_b,
                          _health_b,
                          _attack_b,
                          _defense_b,
                          _speed_b)
    #* Construct an instance of the Game Class from the third set of local variables.
    #? Starts the game loop as part of the constructor.
    _game = Game(_combatant_a,
                 _combatant_b,
                 _stat_points,
                 _turn_duration)
    

# DRIVER CODE
if __name__ == "__main__":
    main()
    input("[Program Finished]\nPress Enter To Exit.\n") #? This is added to keep the script from exiting after the logic is ran.
else:
    print(f"{__name__} was successfully imported.")
    