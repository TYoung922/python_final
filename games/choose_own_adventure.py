# print(r'''
#  ____________________________________________________________________
#  / \-----     ---------  -----------     -------------- ------    ----\
#  \_/__________________________________________________________________/
#  |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
#  |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
#  | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
#  |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
#  |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
#  |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
#  |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
#  |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
#  | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
#  |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
#  |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
#  | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
#  |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
#  | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
#  |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
#  | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
#  |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
#  | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
#  |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
#  |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
#  / \----- ----- ------------  ------- ----- -------  --------  -------\
#  \_/__________________________________________________________________/
# ''')

def start_adventure():
    starting_prompt = ""
    starting_prompt += "\nWelcome to Treasure Island."
    starting_prompt += "\nYour mission is to find the treasure. \n\nYou're at a cross road. where do you want to go? \nType 'left' or 'right' \n"
    return starting_prompt

def adventure(choice):
    result = ""

    if choice == "left":
        result += ("\nYou've come to a lake. There is an island in the middle of the lake.\n"
                   "Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")


    elif choice == "wait":
        result += "\nyou arrive at the island unharmed. There is a house with 3 doors."
        result += "\nOne red, one yellow and one blue. Which colour do you choose? \n"

    elif choice == "red":
        result += "\nFire shoots from the door burning you. \n Game Over!"
    elif choice == "blue":
        result += "\nYou are Eaten by beasts. \n Game Over!"
    elif choice == "yellow":
        result += "\nYou enter a room full of treasure. \n There are probably no mimics... \n YOU WIN!!"
    elif choice == "swim":
        result += "\nAs you are swimming towards the island you see something sparkling deep in the water"
        result += "\nType 'dive' to swim down and investigate or 'ignore' to keep swimming to the island? \n"
    elif choice == "dive":
        result += "\nYou find a strange looking glass orb that glows slightly."
        result += "\nType 'grab' to pick up the orb or type 'surface' to ignore the orb and swim back up\n"
    elif choice == "surface":
        result += "\nyou reach the surface but the island is gone"
        result += "\nType 'try' to try and swim to where the island was or 'back' to swim back to shore\n"
    elif choice == "back":
        result += "\nYou reach the shore safely, but feel that something was lost \n you head home without any treasure,\n"\
                  "but at least you're alive. \n Game Over."
    elif choice == 'try':
        result += "\nAs you get to where the island had been you realize the shore is gone too. \n"\
                  "you try to search for it but are unable to find the land again and eventually drown. \n"\
                  "Game Over!"
    elif choice == 'grab':
        result += "\nYou grab the orb and heave upward finding that a strange tentacle is attached to the orb. \n"\
                  "Out of the sand comes an enormous fish with huge pointed teeth the orb and tentacle attached to its head. \n"\
                  "The fish eats you \n Game Over!"
    elif choice == 'ignore':
        result += "\nyou arrive at the island unharmed. There is a house with 3 doors."
        result += "\nOne orange, one brown and one green. Which colour do you choose? \n"

    elif choice == "orange":
        result += "\nFire shoots from the door burning you. \n Game Over!"
    elif choice == "green":
        result += "\nA swarm of wild beasts emerge quickly devouring you. \n Game Over!"
    elif choice == "brown":
        result += "\nYou enter an empty room. \n As you look around you hear a loud clinking sound above you \n"\
                  "You look up to see a giant treasure chest tipping to dump its contents. \n"\
                  "You try to flee but aren't quick enough. The treasure crushes you.  \n Game Over!"
    elif choice == 'right':
        result += "\nYou find some old ruins"
        result += "\nType 'in' to investigate the ruins or type 'continue' to keep searching\n"
    elif choice == "in":
        result += "\nThe ruins look ancient most of the wooden doors are rotted away. \n"\
                  "You find a door that is still intact, though barely. It won't open"
        result += "\nType 'bash' to attempt to bash the door open or type 'move on' to look elsewhere\n"
    elif choice == "bash":
        result += "\nYou take a running start and throwing your shoulder against the door bust through it in a shower of splinters. \n"\
                  "Inside is a single treasure chest that has miraculously withstood the march of time."
        result += "\nType 'open' to open the treasure chest or type 'leave alone' to leave the chest and continue searching\n"
    elif choice == "open":
        result += "\nYou open the chest to see rows of gleaming pointed teeth within. \nYou are eaten by the mimic. \nGame over!"
    elif choice == "leave alone":
        result += "\nAs you look around your mind wonders if you should have opened the chest after all.\n"\
                  "Distracted you fail to notice the giant spider web.\n"\
                  "stuck in the spider's web you are unable to get away as the spider wraps you up.\n Game Over!"
    elif choice == 'move on':
        result += "\nYou find nothing else in the ruins and decide to leave.\n"\
                  "As you exit out the front a loose stone gives way and you topple over the railing into the chasm below\nGame Over!"
    elif choice == 'continue':
        result += "\nYou find a dragon's nest with large gleaming eggs inside."
        result += "\nType 'take' to go take an egg or type 'leave egg' to keep going.\n"
    elif choice == "leave egg":
        result += "\nYou come to a large mountain. As you look up something gleams brightly catching the light"
        result += "\nType 'climb' to climb the mountain towards the gleam or type 'pass' to move on.\n"
    elif choice == "climb":
        result += "\nAs you climb upward the air quickly grows cold. Your fingers grow numb and you loose your grip galling to your death.\n"\
                  "Game Over!"
    elif choice == "pass":
        result += "\nEverything on this adventure seems far to dangerous you decide to head home.\n"\
                  "You gained no treasure but kept your life.\n"\
                  "Game Over."
    elif choice == "take":
        result += "\nThe egg is extremely heavy.\n"\
                  "As you try to cart it off the dragon returns. Hoping to get away you drop the egg and run.\n"\
                  "The egg cracks leaking goop causing you to slip. Lying prone on the ground you watch in horror\n"\
                  "as gleaming teeth come for you.\n"\
                  "Game Over!"

    return result