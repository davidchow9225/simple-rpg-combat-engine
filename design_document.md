<!-----
NEW: Check the "Suppress top comment" option to remove this info from the output.

Conversion time: 0.532 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β31
* Thu Aug 26 2021 19:36:20 GMT-0700 (PDT)
* Source doc: Simple RPG
----->



# Simple RPG


## A turn-based combat engine that highlights the functionality of object-oriented python.


# Object Classes Required


## **Game()**


### **<span style="text-decoration:underline;">Description</span>**

Class containing the game timer, as well as the ability to modify the attributes of other objects.


### **<span style="text-decoration:underline;">Attributes</span>**


#### **Game.is_running**

Handles the game loop; is modified at the initialization and termination of a game instance.


#### **Game.combatant_a**

The first of two combatants, typically being the player.


#### **Game.combatant_b**

The second of two combatants, typically being the AI opponent.


#### **Game.stat_points**

The amount of points players are given to allocate into their stats at the beginning of the combat.


#### **Game.turn_duration**

The duration, in seconds, that a combatant has to act before having its turn skipped.


### **<span style="text-decoration:underline;">Properties</span>**


### **<span style="text-decoration:underline;">Methods</span>**


#### **Game.__init__(self, _combatant_a, _combatant_b, \*\*modifiers)**

Sets the combatants & modifiers, beginning **_Game.main_loop()_** when everything is in place.


#### **Game.main_loop(self)**

The loop that handles the game timer and object interactions.


#### 


## **Entity()**


### **<span style="text-decoration:underline;">Description</span>**

Base Class for combatant objects.


### **<span style="text-decoration:underline;">Attributes</span>**


#### **Entity._name**

Internal variable for use in the **_Entity.name_** property.


#### **Entity._health**

Internal variable for use in the **_Entity.health_** property.


#### **Entity.attack**

Variable for external use in the **_Game_** object.


#### **Entity.defense**

Variable for external use in the **_Game_** object.


#### **Entity.speed**

Variable for external use in the **_Game_** object.


### **<span style="text-decoration:underline;">Properties</span>**


#### **Entity.health**

Applies special logic to the modification of **_Entity._health_**, ensuring it never drops below zero.


#### **Entity.name**

Applies special logic to the modification of **_Entity._name_**, ensuring string-friendly clean-up code.


### **<span style="text-decoration:underline;">Methods</span>**


#### Entity.__init__(self, _name, _health, _attack, _defense, _speed)

Constructs the combatant, setting its attributes & properties to the provided values.


## **Player(_Entity_)**


### **<span style="text-decoration:underline;">Description</span>**

**_Entity_** subclass with interactive functionality.


### **<span style="text-decoration:underline;">Properties</span>**


### **<span style="text-decoration:underline;">Methods</span>**


#### Player.__init__(self, _name, _health, _attack, _defense, _speed)

Constructs the combatant, setting its attributes & properties to the provided values.
