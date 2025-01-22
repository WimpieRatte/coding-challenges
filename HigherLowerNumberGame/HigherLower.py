#Higher or Lower Number Game - www.101computing.net/higher-or-lower-number-game/
from random import randint

numberToGuess = randint(1,100)
userGuess = -1
while numberToGuess != userGuess:
    userGuess = int(input("Enter a number:"))
    if numberToGuess > userGuess:
        print("Higher!")
    elif numberToGuess < userGuess:
        print("Lower!")
    else:
        print("You Win!")
