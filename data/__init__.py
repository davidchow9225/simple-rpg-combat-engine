"""<Module "Simple RPG/data/__init__.py">
Description:
__init__ file for the data package.
"""
# IMPORTS
#import [Module/Package]
from .objects import __init__


# MAIN METHOD
def main():
    """<Module "Simple RPG/data/__init__.main()">
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
    