#
#   "Ask the user for a string and print out whether this string is a palindrome or not.
#    (A palindrome is a string that reads the same forwards and backwards.)"
#

text = raw_input("Please input a string of text: ")

if text == (text[::-1]):
    print "This string of text is a palindrome"
else:
    print "This string of text is not a palindrome"
