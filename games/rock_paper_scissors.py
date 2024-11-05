import random

rock = """
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """
paper = """
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """
scissors = """
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """
def ropasc_start():
    print("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors")

def ropasc_game(choice):
    player = choice
    computer = random.randint(0, 2)
    result = ""

    if player == 0:
        result += "you chose" + rock
    elif player == 1:
        result += "you chose" + paper
    elif player == 2:
        result += "you chose" + scissors

    result += "\nComputer chose:\n"
    if computer == 0:
        result += rock
    elif computer == 1:
        result += paper
    elif computer == 2:
        result += scissors

    if player == 0 and computer == 0:
        result += "\nIt's a tie."
    elif player == 1 and computer == 0:
        result += "\nYou Win!"
    elif player == 2 and computer == 0:
        result += "\nComputer Wins"

    if player == 0 and computer == 1:
        result += "\nComputer Wins."
    elif player == 1 and computer == 1:
        result += "\nIt's A Tie"
    elif player == 2 and computer == 1:
        result += "\nYou Win!"

    if player == 0 and computer == 2:
        result += "\nYou Win."
    elif player == 1 and computer == 2:
        result += "\nComputer Wins."
    elif player == 2 and computer == 2:
        result += "\nIt's A Tie"

    return result
