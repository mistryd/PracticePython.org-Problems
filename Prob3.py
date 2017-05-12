#
#   "Take a list and write a program that prints out all the elements of the list that are less than 5."
#

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
newList = []

for x in list:
    if x < 5:
        newList.append(x)

print newList
