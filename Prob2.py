#
#   "Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message
#    to the user."
#

num = int(raw_input("Please input any number: "))

if (num % 2) == 0:
    print "\nYou have selected an even number"
else:
    print "\nYou have selected an odd number"