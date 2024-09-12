import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['paper',    'spock'],
    'spock':    ['rock',     'scissors'],
}

def prompt(message):
    print(f"==> {message}")

def player_wins(player_choice, computer_choice):
    return computer_choice in WINNING_COMBOS[player_choice]

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if player_wins(player, computer):
        print('You win!')
    elif player == computer:
        print("It's a tie!")
    else:
        print("Computer wins!")

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()
    while not (answer.startswith('n') or answer.startswith('y')):
        prompt("That's not a valid choice")
        answer = input()

    if answer[0] == 'n':
        break