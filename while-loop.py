import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
# asking user to enter a number from 1 to 10
# generating a random number from 1 to 10
number = random.randint(1,10)

isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        # If the user has guessed the correct answer, exit the loop.
        isGuessRight = True
    else:
        # If the user has not guessed the correct answer, enter the loop.
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
