from flask import Flask, render_template, request


app = Flask(__name__)

process = None

# This variable will store input data
user_input = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

from games.blackjack import play_again, player_draw, result
@app.route('/blackjack', methods=['GET', 'POST'])
def blackjack():
    starting_hand = ""
    if request.method == 'GET':
        starting_hand = play_again()

    result = ""
    if request.method == 'POST':
        action = request.form.get("action")
        result = player_draw(action)

    return render_template("blackjack.html", starting_hand=starting_hand, result=result)

from games.choose_own_adventure import adventure, start_adventure
@app.route('/choose', methods=['GET', 'POST'])
def choose():
    starting_prompt = ""
    if request.method == 'GET':
        starting_prompt = start_adventure()


    result = ""
    if request.method == 'POST':
        choice = request.form.get('choice')
        result = adventure(choice)
    return render_template("choose.html", result=result, starting_prompt=starting_prompt)

from games.hangman import hangman_game, hangman_start
@app.route('/hangman', methods=['GET', 'POST'])
def hangman():
    current_word = ""
    if request.method == 'GET':
        current_word = hangman_start()


    result = ""
    if request.method == 'POST':
        choice = request.form.get('choice')
        result = hangman_game(choice)
    return render_template("hangman.html", result=result, current_word=current_word)

from games.rock_paper_scissors import ropasc_game
@app.route('/roPaSc', methods=['GET', 'POST'])
def ropasc():
    result = ""
    if request.method == 'POST':
        try:
            choice = int(request.form.get('choice'))
            if choice in [0, 1, 2]:
                result = ropasc_game(choice)
            else:
                result = 'Invalid choice. Please choose 0, 1, or 2.'
        except ValueError:
            result = "please enter a valid number."
    return render_template("roPaSc.html", result=result)

from games.number_guess import start_game, guessing
@app.route('/numberguess', methods=['GET', 'POST'])
def numberguess():
    prompt = ""
    message = ""
    if request.method == 'GET' and 'difficulty' in request.args:
        difficulty = request.args.get('difficulty')
        message = start_game(difficulty)

    elif request.method == 'POST':
        guess = int(request.form.get("guess"))
        prompt = guessing(guess)

    return render_template("numberguess.html", message=message, prompt=prompt)

from games.higher_lower import begin_game, higher_lower
@app.route('/higherlower', methods=['GET', 'POST'])
def higherlower():
    starting_prompt = ""
    if request.method == 'GET':
        starting_prompt = begin_game()

    result = ""
    if request.method == 'POST':
        action = request.form.get("action")
        result = higher_lower(action)

    return render_template("higherlower.html", starting_prompt=starting_prompt, result=result)



if __name__ == '__main__':
    app.run(debug=True)



