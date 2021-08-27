"""<Module "Simple RPG/game/objects/game.py">
Description:
Contains the class for Game() objects.
"""
# IMPORTS
#import [Module/Package]


class Game(object):
    #? Constructor
    def __init__(self, _combatant_a, _combatant_b, **modifiers):
        """<Method "Simple RPG/data/objects/game.Game.__init__()">
        Description:
        Sets the combatants & modifiers, beginning Game.main_loop() when everything is in place.
        Args:
            _combatant_a (Object): The first of two combatants, typically being the player.
            _combatant_b (Object): The second of two combatants, typically being the AI opponent.
        """
        #TODO: Set self.stat_points & self.turn_timer to the values of their respective keys within **modifiers
        self.combatant_a = _combatant_a
        self.combatant_b = _combatant_b
        self.stat_points = modifiers.get('stat_points', 15)
        self.turn_duration = modifiers.get('turn_duration', 300)
    def main_loop(self):
        """<Method "Simple RPG/data/objects/game.Game.main_loop()">
        Description:
        Starts the game instance, choosing the combatant with the highest speed attribute to go first.
        This method also assigns timers to each of the players, resetting them when their turn is submitted.
        """
        pass
        

# MAIN METHOD
def main():
    """<Method "Simple RPG/data/objects/game.main()">
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
    