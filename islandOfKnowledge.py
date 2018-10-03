# Call two arms equally strong if the heaviest weights they each are able
# to lift are equal.

# Call two people equally strong if their strongest arms are equally strong
# (the strongest arm can be both the right and the left), and so are their
# weakest arms.

# Given your and your friend's arms' lifting capabilities find out if you
# two are equally strong.

# Example

# For yourLeft = 10, yourRight = 15, friendsLeft = 15, and friendsRight = 10,
# the output should be areEquallyStrong(yourLeft, yourRight, friendsLeft,
# friendsRight) = true;

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return max(yourLeft,yourRight)==max(friendsLeft,friendsRight) and min(yourLeft,yourRight)==min(friendsRight,friendsLeft)




# Given an array of integers, find the maximal absolute difference between any
# two of its adjacent elements.

# Example

# For inputArray = [2, 4, 1, 0], the output should be
# arrayMaximalAdjacentDifference(inputArray) = 3.

def arrayMaximalAdjacentDifference(inputArray):
    maxdiff = 0
    uno = 0
    dos = 1

    for i in range(0,len(inputArray)-1):
        if maxdiff < abs(inputArray[uno] - inputArray[dos]):
            maxdiff = abs(inputArray[uno] - inputArray[dos])
        uno += 1
        dos += 1

    return maxdiff
