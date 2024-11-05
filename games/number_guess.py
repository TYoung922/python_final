import random

# difficulty = None
# print("Welcome to the Number Guessing Game")
# difficulty_setting = input("Choose a difficulty. 'Easy' or 'Hard'? ").lower()

thinking = 0
life = 0

def start_game(difficulty):
    global life, thinking
    message = ""
    if difficulty == 'easy':
        life = 10
    elif difficulty == 'hard':
        life = 5
    thinking = random.randint(1, 101)
    message += "New number selected\n"
    message += f"You have {life} guesses remaining\n"
    return message



def guessing(guess):
    global life, thinking
    prompt = ""
    # prompt += f"You have {life} attempts remaining to guess"
    if guess != thinking and life > 0:
        life -= 1
        if life == 0:
            prompt = f"That's wrong.\nThe answer was {thinking}"
            prompt += "\nYou're out of guesses. Please try again"
        elif guess < thinking:
            prompt += "Too low.\n"
            prompt += f"You have {life} attempts remaining;"
        elif guess > thinking:
            # life -= 1
            prompt += "Too high.\n"
            prompt += f"You have {life} attempts remaining;"
        # else:
        #     prompt += f"You got it!\n"
    elif guess == thinking:
        prompt += f"You got it!\n"
        prompt += f"The answer was {thinking}"
    else:
        prompt += f"You loose. The number was {thinking}"

    return prompt




