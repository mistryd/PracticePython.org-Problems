#
#   "Take two lists and write a program that returns a list that contains only the elements that are common between
#    the lists(without duplicates). Make sure your program works on two lists of different sizes."
#

list = [2,6,10,9,7,44,0]
list2 = [10,9,8,7,6,5,4,3,2,1]

longerList = []
shorterList = []

commonList = []

if len(list) > len(list2):
    longerList = list
    shorterList = list2
else:
    longerList = list2
    shorterList = list

for x in longerList:
    if x in shorterList:
        commonList.append(x)

commonList.sort()

print commonList

