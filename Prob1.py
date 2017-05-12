#
#   "Create a program that asks the user to enter their name and their age. Print out a message addressed to them
#    that tells them the year that they will turn 100 years old."
#

name = raw_input("What is your name?\n")
age = int(raw_input("What is your age?\n"))

current_year = 2017

deltaYears = 100 - age

year_100 = current_year + deltaYears

print "\n" + name + ", you will turn 100 in the year " + str(year_100)


