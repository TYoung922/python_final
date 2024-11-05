from flask import Flask, render_template, request, redirect, url_for
# from flask_socketio import SocketIO, emit
import subprocess
import os

my_secret = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = my_secret
# socketio = SocketIO(app)

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

# @socketio.on('start_game')
# def start_game():
#     global process
#     process = subprocess.Popen(['python', 'games/blackjack.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, text=True)
#
#     for line in process.stdout:
#         socketio.emit('game_output', line.strip())
#
# @socketio.on('send_input')
# def receive_input(user_input):
#     global process
#     process.stdin.write(user_input + "\n")
#     process.stdin.flush()
#     output = process.stdout.readline().strip()
#     socketio.emit('game_output', output)


if __name__ == '__main__':
    app.run(debug=True)


# import subprocess
# from flask import Flask, render_template
# from flask_socketio import SocketIO, emit
# import threading
# import os
#
# my_secret = os.getenv('SECRET_KEY')
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = my_secret
# socketio = SocketIO(app)
#
# # Dictionary to store the process instance
# process_dict = {}
#
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return render_template("index.html")
#
#
# @app.route('/blackjack', methods=['GET', 'POST'])
# def blackjack():
#     return render_template("blackjack.html")
#
# # import asyncio
# #
# # @socketio.on('start_game')
# # def start_game():
# #     process = subprocess.Popen(
# #         ['python', 'games/blackjack.py'],
# #         stdout=subprocess.PIPE,
# #         stdin=subprocess.PIPE,
# #         text=True,
# #         bufsize=1,
# #         universal_newlines=True
# #     )
# #     process_dict['blackjack'] = process
# #
# #     async def read_output():
# #         while True:
# #             line = await asyncio.get_event_loop().run_in_executor(None, process.stdout.readline)
# #             if not line:
# #                 break
# #             socketio.emit('game_output', line.strip())
# #
# #     socketio.start_background_task(read_output)
#
# @socketio.on('start_game')
# def start_game():
#     # Start the game process and store it in process_dict
#     process = subprocess.Popen(
#         ['python', 'games/blackjack.py'],
#         stdout=subprocess.PIPE,
#         stdin=subprocess.PIPE,
#         text=True
#     )
#     process_dict['blackjack'] = process  # store process in dictionary
#
#     # Start a separate thread to continuously read output from the process
#     def read_output():
#         for line in process.stdout:
#             socketio.emit('game_output', line.strip())
#
#     output_thread = threading.Thread(target=read_output)
#     output_thread.start()
#
# @socketio.on('send_input')
# def receive_input(user_input):
#     # Access the stored process and send input to it
#     process = process_dict.get('blackjack')
#     if process and process.stdin and process.stdout:
#         process.stdin.write(user_input + "\n")
#         process.stdin.flush()
#
#         # Optionally, read any immediate response
#         output = process.stdout.readline().strip()
#         socketio.emit('game_output', output)
#     else:
#         socketio.emit('game_output', "Error: Game process not running.")
#
#
# @app.route('/choose', methods=['GET', 'POST'])
# def choose():
#     return render_template("choose.html")
#
# @socketio.on('start_game')
# def start_game():
#     # Start the game process and store it in process_dict
#     process = subprocess.Popen(
#         ['python', 'games/choose.py'],
#         stdout=subprocess.PIPE,
#         stdin=subprocess.PIPE,
#         text=True
#     )
#     process_dict['choose'] = process  # store process in dictionary
#
#     # Start a separate thread to continuously read output from the process
#     def read_output():
#         for line in process.stdout:
#             socketio.emit('game_output', line.strip())
#
#     output_thread = threading.Thread(target=read_output)
#     output_thread.start()
#
# @socketio.on('send_input')
# def receive_input(user_input):
#     # Access the stored process and send input to it
#     process = process_dict.get('choose')
#     if process and process.stdin and process.stdout:
#         process.stdin.write(user_input + "\n")
#         process.stdin.flush()
#
#         # Optionally, read any immediate response
#         output = process.stdout.readline().strip()
#         socketio.emit('game_output', output)
#     else:
#         socketio.emit('game_output', "Error: Game process not running.")
#
# if __name__ == '__main__':
#     socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
