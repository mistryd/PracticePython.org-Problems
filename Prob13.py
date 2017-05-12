#
#   "Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this
#    opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in
#    the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the
#    sequence is the sum of the previous two numbers in the sequence. The sequence looks like this:
#    1, 1, 2, 3, 5, 8, 13, etc)"
#

def makeFibLis(length):
    if length == 0:
        fibList = []
        return fibList
    elif length == 1:
        fibList = [1]
        return fibList

    fibList = [1,1]
    num = 1
    for x in range(1, length - 1):
        num = fibList[len(fibList) - 1] + fibList[len(fibList) - 2]
        fibList.append(num)

    return fibList

userLength = int(raw_input("Enter how many sequential Fibonnaci numbers you would like to see: "))

print makeFibLis(userLength)

