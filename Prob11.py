#
#   "Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime
#    number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take
#    this opportunity to practice using functions, described below."
#

def isPrime(num):
    divisors = []

    for x in range(1,(num + 1)):
        if (num % x) == 0:
            divisors.append(x)

    return divisors


userNum = int(raw_input("If you want to find out if a number is prime, enter it here and we'll find out: "))

if len(isPrime(userNum)) <= 2:
    print "That is a prime number!"
else:
    print "That is not a prime number!"
    print "It is divisble by: ", isPrime(userNum)