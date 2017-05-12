#
#   "Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix
#    of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new
#    password every time the user asks for a new password. Include your run-time code in a main method."
#

#   Creating a password that is between 8 and 12 characters long and has at least one lowercase char, one uppercase char,
#   and one num

import random as rnd

lenOfPass = rnd.randint(8,12)

numOfLower = rnd.randint(1,(lenOfPass - 2))

lenOfPassRemaining = lenOfPass - numOfLower

numOfUpper = rnd.randint(1,(lenOfPassRemaining - 1))

lenOfPassRemaining = lenOfPassRemaining - numOfUpper

numOfNum = lenOfPassRemaining

password = []

for x in range(0, numOfUpper):

    password.append(chr(rnd.randint(65,90)))

for x in range(0, numOfLower):

    password.append(chr(rnd.randint(97,122)))

for x in range(0, numOfNum):

    password.append(chr(rnd.randint(48,57)))

rnd.shuffle(password)

strPassword = "".join(password)

print "Your randomly generated secure password is:", strPassword
