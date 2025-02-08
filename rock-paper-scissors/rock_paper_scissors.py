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

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def prompt(message):
    print(f'==> {message}')

def get_player_choice():

    def choice_legend():
        """
        To create the legend for each choice.
        For example, the legend for the choice "scissors" is "[Sc]issors". 
        """

        choice_legends = []

        for choice, word in CHOICE_TO_WORD.items():
            legend = f'[{choice.title()}]{word[len(choice):]}'
            choice_legends.append(legend)

        return choice_legends

    while True:
        prompt(f"Choose one:  {'  '.join(choice_legend())}")
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

def display_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        prompt("It's a tie!")
    elif computer_choice in CHOICES_TO_WIN[player_choice]:
        prompt("You win!")
    else:
        prompt("Computer wins!")

def ask_play_again():
    while True:
        prompt("Would you like to play again?")
        prompt("Choose one:  [Y]es  [N]o")
        play_again = input().strip().lower()

        if play_again.startswith('y') or play_again.startswith('n'):
            break

        prompt("You must choose either y or n.")

    return play_again

def run_game():
    clear()
    prompt("Welcome to Rock Paper Scissors Lizard Spock!")

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        display_players_choices(player_choice, computer_choice)
        display_winner(player_choice, computer_choice)

        play_again = ask_play_again()
        clear()
        if play_again.startswith("n"):
            break

    prompt("Thank you for playing. Goodbye!")

run_game()