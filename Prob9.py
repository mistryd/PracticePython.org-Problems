#
#   "Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
#    whether they guessed too low, too high, or exactly right."
#

import random as rnd

correctNum = rnd.randint(1,9)

userNum = int(raw_input("Please guess an integer from 1 to 9 inclusive: "))

if userNum == correctNum:
    print "Congrats you chose the right number!"
elif userNum > correctNum:
    print "Oh no, your number is too high! The correct answer was", correctNum
else:
    print "Oh no, your number is too low! The correct answer was", correctNum
