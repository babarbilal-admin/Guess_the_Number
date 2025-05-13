# This is a Guess the Number game.
import random
from time import sleep

while True:
    play = input('Would you like to play Guess the Number game? (yes/no)').strip()

    if play.lower() == 'no':
        break
    else:        
        guessestaken = 0

        print('Hello! What is your name?')
        myName = input()

        number = random.randint(1, 20)
        print('Well, '+myName+', I am thinking of a number between 1 and 20.')

        for guessestaken in range(6):
            print('Take a guess.')
            try:
                guess = int(input())
            except:
                print('Invalid input! Please input a valid number.')
            else:
                if guess < number:
                    print('Your guess is too low.')
                elif guess > number:
                    print('Your guess is too high.')
                else:
                    break

        if guess == number:
            guessestaken = str(guessestaken + 1)
            print('Good Job, '+myName+'! You guessed my number in ' +guessestaken+ ' guesses!')

        if guess != number:
            number = str(number)
            print('Nope. The number I was thinking of was ' +number+ '.')

        sleep(3.0)