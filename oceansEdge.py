# Given an array of integers, find the pair of adjacent elements that
# has the largest product and return that product.

# Example

# For inputArray = [3, 6, -2, -5, 7, 3], the output should be
# adjacentElementsProduct(inputArray) = 21.

# 7 and 3 produce the largest product

def adjacentElementsProduct(inputArray):
    macs = -100000
    for i in range(len(inputArray)):
        if i == len(inputArray)-1:
            return macs
        elif inputArray[i] * inputArray[i+1] > macs:
            macs = inputArray[i] * inputArray[i+1]
    return macs






# Below we will define an n-interesting polygon.
# Your task is to find the area of a polygon for a given n.

# A 1-interesting polygon is just a square with a side of length 1.
# An n-interesting polygon is obtained by taking the n - 1-interesting
# polygon and appending 1-interesting polygons to its rim, side by side.

# Example

# For n = 2, the output should be
# shapeArea(n) = 5;
# For n = 3, the output should be
# shapeArea(n) = 13.

def shapeArea(n):
     return n**2 + (n-1)**2





# Ratiorg got statues of different sizes as a present from CodeMaster
# for his birthday, each statue having an non-negative integer size.
# Since he likes to make things perfect, he wants to arrange them from
# smallest to largest so that each statue will be bigger than the previous
# one exactly by 1. He may need some additional statues to be able to
# accomplish that. Help him figure out the minimum number of additional
# statues needed.

# Example

# For statues = [6, 2, 3, 8], the output should be
# makeArrayConsecutive2(statues) = 3.

# Ratiorg needs statues of sizes 4, 5 and 7.
def makeArrayConsecutive2(statues):
    count = 0
    place = min(statues)

    for i in range(min(statues),max(statues)+1):
        if place == max(statues):
            return count
        else:
            place += 1
            if place not in statues:
                count += 1







# Given a sequence of integers as an array, determine whether it is possible
# to obtain a strictly increasing sequence by removing no more than one element
# from the array.

# Example

# For sequence = [1, 3, 2, 1], the output should be
# almostIncreasingSequence(sequence) = false.

# There is no one element in this array that can be removed in order to get
# a strictly increasing sequence.

# For sequence = [1, 3, 2], the output should be
# almostIncreasingSequence(sequence) = true.

# You can remove 3 from the array to get the strictly increasing sequence
# [1, 2]. Alternately, you can remove 2 to get the strictly increasing
# sequence [1, 3].
def first_bad_pair(sequence):
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i
    return -1

def almostIncreasingSequence(sequence):
    j = first_bad_pair(sequence)
    if j == -1:
        return True
    if first_bad_pair(sequence[j-1:j] + sequence[j+1:]) == -1:
        return True
    if first_bad_pair(sequence[j:j+1] + sequence[j+2:]) == -1:
        return True
    return False




# After they became famous, the CodeBots all decided to move to a new
# building and live together. The building is represented by a rectangular
# matrix of rooms. Each cell in the matrix contains an integer that represents
# the price of the room. Some rooms are free (their cost is 0), but that's probably
# because they are haunted, so all the bots are afraid of them. That is why any
# room that is free or is located anywhere below a free room in the same column
# is not considered suitable for the bots to live in.

# Help the bots calculate the total price of all the rooms that are suitable for them.

# Example

# For
# matrix = [[0, 1, 1, 2],
#           [0, 5, 0, 0],
#           [2, 0, 3, 3]]
# the output should be
#
# Here's the rooms matrix with unsuitable rooms marked with 'x':

# [[x, 1, 1, 2],
#  [x, 5, x, x],
#  [x, x, x, x]]
# Thus, the answer is 1 + 5 + 1 + 2 = 9.

# For
# matrix = [[1, 1, 1, 0],
#           [0, 5, 0, 1],
#           [2, 1, 3, 10]]
# the output should be
# matrixElementsSum(matrix) = 9.

# Here's the rooms matrix with unsuitable rooms marked with 'x':

# [[1, 1, 1, x],
#  [x, 5, x, x],
#  [x, 1, x, x]]
# Note that the free room in the first row make the full column unsuitable for bots.

# Thus, the answer is 1 + 1 + 1 + 5 + 1 = 9.
def matrixElementsSum(matrix):
    roomnum = []
    price = 0
    for floor in matrix:
        xroom = 0
        for room in floor:
            if room == 0:
                roomnum.append(xroom)
                xroom += 1
            elif xroom in roomnum:
                xroom += 1
            else:
                price += room
                xroom += 1

    return price
