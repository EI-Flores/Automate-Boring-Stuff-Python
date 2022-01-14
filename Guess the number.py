# This is a simple game where the computer picks a random number between 1 and 10.

import random
print('Hello! What is your name?')
name = input()
secretNumber = random.randint(1, 10)
print('Well, ' + name + ', I am thinking of a number between 1 and 10.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too hight')
    else:
        break # This condition is the correct guess!

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!' + "\n")
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))