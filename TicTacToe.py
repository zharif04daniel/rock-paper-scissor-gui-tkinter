from tkinter import *
import random

print('Welcome to the game! ')
name = input('What is your name? ')
print("Let's go " + name)

options = ['rock','paper','scissors']

computer_wins = 0
user_wins = 0
draws = 0

while True:
    user_pick = input('\nPick Rock/Paper/Scissors or Q to quit: ').lower()
    if user_pick == 'q':
        break

    if user_pick not in options:
        continue

    computer_pick = random.choice(options)
    print('Computer picked ' + computer_pick + '.')

    if user_pick == 'paper' and computer_pick == 'rock':
        print('You won!')
        user_wins += 1

    elif user_pick == 'rock' and computer_pick == 'scissors':
        print('You won!')
        user_wins += 1
    elif user_pick == 'scissors' and computer_pick == 'paper':
        print('You won!')
        user_wins += 1

    elif user_pick == computer_pick:
        print('Draw!')
        draws += 1

    else:
        print('Computer won!')
        computer_wins += 1

print('\nYou won ' + str(user_wins) + ' times')
print('Computer won ' + str(computer_wins) + ' times')
print('Draws ' + str(draws) + ' times')
print('\nThank You ' + name + '!')