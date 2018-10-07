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


# IPv4 addresses are represented in dot-decimal notation, which consists of
# four decimal numbers, each ranging from 0 to 255 inclusive, separated by
# dots, e.g., 172.16.254.1.

# Given a string, find out if it satisfies the IPv4 address naming rules.

# Example
# For inputString = "172.16.254.1", the output should be
# isIPv4Address(inputString) = true;

def isIPv4Address(inputString):
    nums = inputString.split(".")

    for n in nums:
        if n == '' or n.isdigit()==False or len(nums) != 4:
            return False
        elif int(n) not in range(0,256):
            return False

    return True


#  You are given an array of integers representing coordinates of obstacles
#  situated on a straight line.  Assume that you are jumping from the point
#  with coordinate 0 to the right. You are allowed only to make jumps of the
#  same length represented by some integer.

#  Find the minimal length of the jump enough to avoid all the obstacles.

#  Example

#  For inputArray = [5, 3, 6, 7, 9], the output should be
#  avoidObstacles(inputArray) = 4.

def avoidObstacles(inputArray):
    jump = 2
    bunny = 0

    while bunny < max(inputArray)+1:
        print(jump)
        print(bunny)
        if bunny in inputArray:
            bunny = 0
            jump += 1
            print(bunny)
        else:
            bunny += jump
            print(jump)
            print(bunny)
    return jump
