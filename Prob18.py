#
#   "Create a program that will play the cows and bulls game with the user. The game works like this: Randomly generate
#    a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in
#    the correct place, they have a cow. For every digit the user guessed correctly in the wrong place is a bull.
#    Every time the user makes a guess, tell them how many cows and bulls they have. Once the user guesses the
#    correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell
#    the user at the end."
#

import random as rnd

gameState = True

print "Hello and Welcome to Cows and Bulls"

correct = str(rnd.randint(1000,9999))

cows = 0
bulls = 0

while gameState:
    userNum = raw_input("Please enter a 4 digit number: ")

    for x in range(0,4):
        if correct[x] == userNum[x]:
            cows = cows + 1
        else:
            bulls = bulls + 1

    print "You have", cows, "cows and", bulls, "bulls"

    if cows == 4:
        print "You won!"
        gameState = False

    cows = 0
    bulls = 0






