import random
import sys
from time import sleep

computer_choice = random.randint(0,2)

if computer_choice == 0:
        computer_choice = 'rock'

if computer_choice == 1:
        computer_choice = 'paper'

if computer_choice == 2:
        computer_choice = 'scissors'


def decide_winner(choice, computer_choice):
    print('you selected: %s' % choice)
    print('computer selecting...')
    sleep(1)
    print('computer selected: %s' % computer_choice)

    if choice == computer_choice:
        print(f'both players selected {choice}. it''s a draw!')

    elif choice == 'rock':
        if computer_choice == 'scissors':
            print('rock beats scissors! you win!')
        else:
            print('paper beats rock! you lose!')
    elif choice == 'paper':
        if computer_choice == 'rock':
            print('paper beats rock! you win!')
        else:
            print('scissors beats paper! you lose!')
    elif choice == 'scissors':
        if computer_choice == 'paper':
            print('scissors beats paper! you win!')
        else:
            print('rock beats scissors! you lose!')

def rps_game():
    choice = input('R, P or S? :  ')
    choice = choice.upper()
    if choice == 'R':
        choice = 'rock'
    if choice == 'S':
        choice = 'scissors'
    if choice == 'P':
        choice = 'paper'

    decide_winner(choice, computer_choice)

rps_game()

while True:
    replay = input('play again? (y/n): ')
    if replay.lower() != 'y':
        sys.stdout()
    if replay.lower() == 'y':
        rps_game()

















