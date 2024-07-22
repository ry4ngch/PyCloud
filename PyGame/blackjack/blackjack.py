import random
import os
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    rand_card = random.choice(cards)
    return rand_card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > 21:
        return "You went over, You Lose"
    elif user_score == computer_score:
        # it is a draw
        return "Draw"
    elif computer_score == 0:
        return "Opponent has Blackjack, You lose"
    elif user_score == 0:
        return "You have blackjack, You win"
    elif user_score > computer_score:
        return "You score is higher, you win"
    else:
        return "Opponent score is higher, you lose"

def play_game():
    clear()
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    #deal 2 card to user and computer card each
    for r in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Do you want to add another card?, type 'n' to pass: ")
            if user_should_deal.lower() == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

        if computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer final hand {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    restart_game = input("Do you want to replay the game? [y/n] ").lower()
    if restart_game == "y":
        play_game()
    else:
        print("Thank you for playing")

play_game()
