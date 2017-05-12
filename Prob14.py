#
#   "Write a program (function!) that takes a list and returns a new list that contains all the elements of the first
#    list minus all the duplicates."
#

lis = ["a", "b", "b", "c", "c", "c", "d", "d", "d", "d"]

lis = set(lis)
lis = list(lis)

print lis
