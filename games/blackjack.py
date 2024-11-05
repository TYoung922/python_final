import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []
player_score = sum(player_hand)
dealer_score = sum(dealer_hand)
player_busted = False
game_over = False

result = ""

def calculate_player():
    global player_score
    player_score = sum(player_hand)
    if 11 in player_hand and player_score > 21:
        player_hand[player_hand.index(11)] = 1
        player_score = sum(player_hand)

def calculate_dealer():
    global dealer_score
    dealer_score = sum(dealer_hand)
    if 11 in dealer_hand and dealer_score > 21:
        dealer_hand[dealer_hand.index(11)] = 1
        dealer_score = sum(dealer_hand)


def player_draw(choice):
    global result
    result = ""
    # result += f"Your cards: {player_hand}, current score: {player_score}"
    # result += "\nType 'y' to get another card, or 'n' to stand: "
    if choice == 'draw':
        player_hand.append(cards[random.randint(0, 12)])
        calculate_player()
        result += f"your cards: {player_hand}, current score: {player_score}"
        result += f"\nDealer first card: {dealer_hand[0]}"
        if player_score == 21:
            finish_game()
        if player_score > 21:
            global player_busted
            player_busted = True
            finish_game()
    elif choice == 'stand':
        finish_game()
    return result

def play_blackjack():
    player_hand.append(cards[random.randint(0, 12)])
    player_hand.append(cards[random.randint(0, 12)])
    dealer_hand.append(cards[random.randint(0, 12)])
    dealer_hand.append(cards[random.randint(0, 12)])
    calculate_player()
    return f"\nStarting hand: {player_hand}, total {player_score}\ndealer showing: {dealer_hand[0]}"
    # player_draw()



def dealer_draw():
    calculate_dealer()
    while dealer_score < 17:  # Keep drawing until dealer's score is 17 or more
        dealer_hand.append(cards[random.randint(0, 12)])
        calculate_dealer()  # Update dealer's score after drawing
    finish_game()


def finish_game():
    global player_busted, result, game_over
    if game_over:
        return
    game_over = True

    result = ""
    calculate_player()
    calculate_dealer()
    if dealer_score < 17 and player_busted == False:
        dealer_draw()

    if player_busted:
        result += f"You busted with {player_hand} score: {player_score}"
        result += f"\nDealer had a hand with {dealer_hand} score: {dealer_score}"
    else:
        result += f"Your final hand: {player_hand}, final score: {player_score}"
        result += f"\nDealer's final hand: {dealer_hand}, final score: {dealer_score}"

        if player_score > 21:
            result += "\nYou busted! Dealer wins."
        elif dealer_score > 21:
            result += "\nDealer busted! You win!"
        elif player_score > dealer_score:
            result += "\nYou win!"
        elif dealer_score > player_score:
            result += "\nDealer wins!"
        else:
            result += "\nIt's a draw!"
    return result



def play_again():
    global player_busted, result, game_over
    player_busted = False
    player_hand.clear()
    dealer_hand.clear()
    result = play_blackjack()
    game_over = False
    return result