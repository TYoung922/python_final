# print(r'''
#  ___________.._______
# | .__________))______|
# | | / /      ||
# | |/ /       ||
# | | /        ||.-''.
# | |/         |/  _  \
# | |          ||  `/,|
# | |          (\\`_.'
# | |         .-`--'.
# | |        /Y . . Y\
# | |       // |   | \\
# | |      //  | . |  \\
# | |     ')   |   |   (`
# | |          ||'||
# | |          || ||
# | |          || ||
# | |          || ||
# | |         / | | \
# """"""""""|_`-' `-' |"""|
# |"|"""""""\ \       '"|"|
# | |        \ \        | |
# : :         \ \       : :
# . .          `'       . .
#  _
# | |
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |
#                    |___/
# ''')

noose_state = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random
word_list = ["aardvark", "baboon", "camel", "apple", "computer", "yellow"]
# word = random.choice(word_list)

# reveal = list(len(word) * "_")
# chosen_word = list(word)
word = ""
reveal = []
chosen_word = []
life = 0

# print("Word to guess:", ''.join(reveal))
# print(word)


def hangman_start():
    global chosen_word
    global reveal
    global life
    global word
    life = 6
    word = random.choice(word_list)
    reveal = list(len(word) * "_")
    chosen_word = list(word)

    current_word = "Word to guess: " + ' '.join(reveal)
    return current_word


def hangman_game(choice):
    global life
    correct_guess = False
    previous_guess = []
    already = False
    result = ""
    player_guess = choice.lower()

    # if life > 0 and

    if life > 0:
        result = "Word to guess:" + ' '.join(reveal)
        if player_guess in previous_guess:
           already = True
        else:
            previous_guess.append(player_guess)
        # print(previous_guess)
        if not already:
            for index, let in enumerate(chosen_word):
                if let == player_guess:
                    reveal[index] = player_guess
                    correct_guess = True
            if correct_guess:
                result = ' '.join(reveal)
                correct_guess = False
            else:
                life -= 1
                if life > 0:
                    result = ' '.join(reveal)
                    result += f"\nYou guessed {player_guess}, that's not in the word. You lose a life."
                else: result = f"\nIt was {word}. You Lose!"
            blank_check = "_"
            if not blank_check in reveal:
                win = True
                result += "\nYou Win!"
                life = -1
            else:
                result += noose_state[life]
                result += f"\n******************************* {life}/6 Lives Left *******************************\n"
        else:
            f"\nyou've already guessed {player_guess}"
            already = False
    else:
        result += "You're out of lives. Try a new word"

    return result
