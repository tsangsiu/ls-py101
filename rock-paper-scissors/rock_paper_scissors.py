import random
import os

CHOICE_TO_WORD = {
    'r': 'rock',
    'p': 'paper',
    'sc': 'scissors',
    'l': 'lizard',
    'sp': 'spock'
}
CHOICES_TO_WIN ={
    'r': ['l', 'sc'],
    'p': ['r', 'sp'],
    'sc': ['p', 'l'],
    'l': ['sp', 'p'],
    'sp': ['sc', 'r']
}
CHOICES = list(CHOICE_TO_WORD.keys())
WINS_NEEDED = 3

"""
To create the legend for each choice.
For example, the legend for the choice "scissors" is "[Sc]issors". 
"""
CHOICE_LEGENDS = [f'[{choice.title()}]{word[len(choice):]}' \
                  for choice, word in CHOICE_TO_WORD.items()]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def prompt(message):
    print(f'==> {message}')

def display_welcome_msg():
    choices_titlized = [choice.title() for choice in CHOICE_TO_WORD.values()]
    game_name = ' '.join(choices_titlized)

    prompt(f"Welcome to {game_name}!")

def display_rule():
    prompt(f"Whoever reaches {WINS_NEEDED} " + \
           f"win{'s' if WINS_NEEDED > 1 else ''} first is the grand winner!")

def get_player_choice():
    while True:
        prompt(f"Choose one:  {'  '.join(CHOICE_LEGENDS)}")
        player_choice = input().strip().lower()

        if player_choice in CHOICES:
            break

        prompt("You must choose either " + \
               f"{', '.join(CHOICES[:-1])} or {CHOICES[-1]}.")

    return player_choice

def get_computer_choice():
    computer_choice = random.choice(CHOICES)
    return computer_choice

def display_players_choices(player_choice, computer_choice):
    prompt(f'You chose {CHOICE_TO_WORD[player_choice]}, ' + \
           f'and computer chose {CHOICE_TO_WORD[computer_choice]}.')

def winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        winner_ = "tie"
    elif computer_choice in CHOICES_TO_WIN[player_choice]:
        winner_ = "player"
    else:
        winner_ = "computer"

    return winner_

def display_round_winner(player_choice, computer_choice):
    winner_ = winner(player_choice, computer_choice)

    match winner_:
        case "player":
            prompt("You win this round!")
        case "computer":
            prompt("Computer wins this round!")
        case "tie":
            prompt("It's a tie!")

def display_grand_winner(scores):
    if scores['player'] == WINS_NEEDED:
        prompt("You are the grand winner!")
    else:
        prompt("Computer is the grand winner!")

def add_score(scores, player_choice, computer_choice):
    winner_ = winner(player_choice, computer_choice)

    match winner_:
        case "player":
            scores['player'] += 1
        case "computer":
            scores["computer"] += 1

def display_scores(scores):
    prompt(f"Your score: {scores['player']}; " + \
           f"Computer score: {scores['computer']}")

def ask_play_again():
    while True:
        prompt("Would you like to play again?")
        prompt("Choose one:  [Y]es  [N]o")
        play_again = input().strip().lower()

        if play_again in ['y', 'n']:
            break

        prompt("You must choose either y or n.")

    return play_again

def display_goodbye_msg():
    prompt("Thank you for playing. Goodbye!")

def game():
    clear()

    display_welcome_msg()
    display_rule()

    # each loop is a game
    while True:
        scores = { 'player': 0, 'computer': 0 }

        # each loop is a round
        while True:
            player_choice = get_player_choice()
            computer_choice = get_computer_choice()

            clear()
            display_players_choices(player_choice, computer_choice)
            display_round_winner(player_choice, computer_choice)
            add_score(scores, player_choice, computer_choice)
            display_scores(scores)

            if WINS_NEEDED in scores.values():
                break

        display_grand_winner(scores)

        play_again = ask_play_again()
        clear()
        if play_again.startswith("n"):
            break

    display_goodbye_msg()

game()