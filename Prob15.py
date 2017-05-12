#
#   "Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to
#    the user the same string, except with the words in backwards order."
#

longString = raw_input("Please enter a long string containing multiple words: ")

listString = longString.split()
listString.reverse()

print " ".join(listString)