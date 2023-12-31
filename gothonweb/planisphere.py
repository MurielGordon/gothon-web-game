#from sys import exit
import app

class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)
    
    def add_paths(self, paths):
        self.paths.update(paths)


central_corridor = Room("Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed you entire crew. 
You are the last surviving member and your last mission is to get the neutron destruct
bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting
into an escape pod.
        
You're running down the central corridor to the Weapons Armory when a Gothon jumps out,
red scaly skin, dark grimy teeth, and evil clow costume flowing around his hate filled
body. He's blocking the door to the Armory and about to pull a weapon to blast you.

To survive this encounter do you shoot, dodge, or tell a joke?
"""
)


laser_weapon_armory = Room("Laser Weapon Armory",
"""
Lucky for you they made you learn Gothon insults in the academy. You tell the one Gothon
joke you know: Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur
ubhfr.  The Gothon stops, tries not to laugh, then burts out laughing and can't more.
While he's laughing you run up and shoot him square in the head putting him down, then 
jump through the Weapon Armory door.

You do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might
be hiding. It's dead quiet, too quiet. You stand up and run to the far side of the room and find 
the neutron bomb in its container.
There's a keypad lock on the box and you need the core to get the bomb out. If you get the code
wrong 10 times then the lock closes forever and you can't get the bomb. The code is 3 digits.
"""
)

guess_again = Room("Guess Again",
"""
BZZZZEDDD!

You got it wrong. Remember, you only have 10 chances to make this work. 
"""                   
)

final_guess = Room("Final Guess",
"""
BZZZZEDDD!

You got it wrong again. This is your last chance to try. 


Hint: Think of a diabolically hot number
"""                   
)


the_bridge = Room("The Bridge",
"""
The container clicks open and the seal breaks, letting gas out. You grab the neutron bomb and
run as fast as you can to the bridge where you must place it in the right spot.

You burst onto the Bridge with the netron destruct bomb under your arm and surprise 5 Gothons who
trying to take control of the ship. Each of them has an even uglier clown costume than the last. 
They haven't pulled their weapons out yet, as they see the active bomb under your arm and don't want
to set it off.

Do you throw the bomb or place it gently?
"""
)


escape_pod = Room("Escape Pod",
"""
You point your blaster at the bomb under your arm and the Gothons put their hands up and start to
sweat. You inch backward to the door, open it, and then carefully place the bomb on the floor,
pointing your blaster at it. You then jump back through the door, punch the close button and blast
the lock so the Gothons can't get out. Now that the bomb is placed you run to the escape pod to get
off this tin can.

You rush through the ship desperately trying to make it to the escape pod before the whole ship explodes.
It seems like hardly any Gothons are on the ship, so your run is clear of interference. You get to the
chamber with the escape pods, and now need to pick one to take. Some of them could be damaged but you
don't have time to look.
There are 5 pods, which one do you take?
"""
)


the_end_winner = Room("The End",
"""
You jump into pod 2 and hit the eject button. The pod easily slides out into space heading to
the planet below. As it flies to the planet, you look back and see your ship implode then explode
like a bright star, taking out the Gothon ship at the same time. You won!
"""
)


the_end_loser = Room("The End",
"""
You jump into pod a random pod and hit the eject button. The pod escaped out into the void of space, then
implodes as the hull ruptures, crushing your body into jam jelly.
"""
)

#generic_death = Room("death", "You died.") 

shoot_death = Room("You chose poorly.", 
"""
Quick on the draw you yank out your blaster and fire
it at the Gothon.  His clown costume is flowing and
moving around his body, which throws off your aim.
Your laser hits his costume but misses him entirely.
This completely ruins his brand new costume his mother
bought him, which makes him fly into an insane rage
and blast you repeatedly in the face until you are
dead.  Then he eats you.
"""
)

dodge_death = Room("You chose poorly.",
"""
Like a world class boxer you dodge, weave, slip and slide right as the Gothon's blaster
cranks a laser past your head. In the middle of your artful dodge your foot slips and
you bang your head on the metal wall and pass out. You wake up shortly after only to die
as the Gothon stomps on your head and eats you.
"""                   
)

code_death = Room("You chose poorly.",
"""
The lock buzzes one last time and then you hear a sickening melting sound as the mechanism is 
fused together. You decide to sit there, and finally the Gothons blow up the ship from their
ship and you die.
"""
)

bomb_death = Room("You chose poorly.",
"""
In a panic you throw the bomb at the group of Gothons and make a leap for the door. Right as you
drop it a Gothon shoots you right in the back killing you. As you die you see another Gothon
frantically try to disarm the bomb. You die knowing they will probably blow up when it goes off.
"""                                    
)

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

the_bridge.add_paths({
    'throw the bomb': bomb_death,
    'place bomb gently': escape_pod
})

final_guess.add_paths({
    "666": the_bridge,
    "*": code_death
})

guess_again.add_paths({
    "666": the_bridge,
    '*': final_guess
})

laser_weapon_armory.add_paths({
    '666': the_bridge,
    '*': guess_again
})

central_corridor.add_paths({
    'shoot!': shoot_death,
    'dodge!': dodge_death,
    'tell a joke': laser_weapon_armory,
})

START = 'central_corridor'

def load_room(name):
    """
    There is a potential security problem here.
    Who gets to set name? Can that expose a variable?
    """
    # pg 278
    return globals().get(name)

def name_room(room):
    """
    Same possible security problem. Can you trust room?
    What's a better solution than this globals lookup?
    """
    for key, value in globals().items():
        if value == room:
            return key
        

#def load_room(name):
#    whitelist = [
#        "central_corridor", "laser_weapon_armory", "the_bridge", "escape_pod", "the_end_winner",
#        "the_end_loser", "generic_death"
#    ]
#    if name in whitelist:
#        return globals().get(name)
#    else:
#        exit(0)

#def name_room(room):
#    whitelist = [
#        central_corridor, laser_weapon_armory, the_bridge, escape_pod, the_end_winner,
#        the_end_loser, generic_death
#    ]
#    if room in whitelist:
#        for key, value in globals().items():
#            if value == room:
#                return key
#    else:
#        exit(0)