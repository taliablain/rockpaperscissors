import random
import sys
from time import sleep

def computer_choice():
    computer_choice = random.randint(0,2)

    if computer_choice == 0:
            computer_choice = 'rock'

    if computer_choice == 1:
            computer_choice = 'paper'

    if computer_choice == 2:
        computer_choice = 'scissors'
    return computer_choice

def user_choice():
    choice = input('R, P or S? :  ')
    choice = choice.upper()
    if choice == 'R':
        choice = 'rock'
        return choice
    if choice == 'S':
        choice = 'scissors'
        return choice
    if choice == 'P':
        choice = 'paper'
        return choice


def decide_winner():
    choice = user_choice()
    computer = computer_choice()
    print('you selected: %s' % choice)
    print('computer selecting...')
    sleep(1)
    print('computer selected: %s' % computer)

    if choice == computer:
        print(f'both players selected {choice}. it''s a draw!')

    elif choice == 'rock':
        if computer == 'scissors':
            print('rock beats scissors! you win!')
        else:
            print('paper beats rock! you lose!')
    elif choice == 'paper':
        if computer == 'rock':
            print('paper beats rock! you win!')
        else:
            print('scissors beats paper! you lose!')
    elif choice == 'scissors':
        if computer == 'paper':
            print('scissors beats paper! you win!')
        else:
            print('rock beats scissors! you lose!')



def rps_game():
    decide_winner()



    while True:
        replay = input('play again? (y/n): ')
        if replay.lower() != 'y':
            sys.exit()
        if replay.lower() == 'y':
            rps_game()

rps_game()

















