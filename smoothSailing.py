# Given an array of strings, return another array containing
# all of its longest strings.

# Example

# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# allLongestStrings(inputArray) = ["aba", "vcd", "aba"]

def allLongestStrings(inputArray):
    max = 0
    newarr = []
    for i in inputArray:
        if len(i) > max:
            max = len(i)
    for i in inputArray:
        if len(i)==max:
            newarr.append(i)
    return newarr




# Given two strings, find the number of common characters between them.

# Example

# For s1 = "aabcc" and s2 = "adcaa", the output should be
# commonCharacterCount(s1, s2) = 3.

# Strings have 3 common characters - 2 "a"s and 1 "c".

def commonCharacterCount(s1, s2):
    total = 0
    first = {}
    second = {}
    for i in s1:
        if i in first:
            first[i]+=1
        else:
            first[i] = 1

    for e in s2:
        if e in second:
            second[e]+=1
        else:
            second[e] = 1

    for a in first:
        if a in second:
            if first[a]<= second[a]:
                total += first[a]
            else:
                total += second[a]

    return total




# Ticket numbers usually consist of an even number of digits. A ticket
# number is considered lucky if the sum of the first half of the digits
# is equal to the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.

# Example

# For n = 1230, the output should be
# isLucky(n) = true;
# For n = 239017, the output should be
# isLucky(n) = false.

def isLucky(n):
    num = str(n)
    A = [int(x) for x in num]
    stop = (len(A)/2)-1
    fir = []
    sec = []
    for i in range(len(A)):
        if i <= stop:
            fir.append(A[i])
        else:
            sec.append(A[i])
    print(fir)
    print(sec)
    if sum(fir) == sum(sec):
        return True
    else:
        return False



# Some people are standing in a row in a park. There are trees between them
# which cannot be moved. Your task is to rearrange the people by their heights
# in a non-descending order without moving the trees. People can be very tall!

# Example

# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
def sortByHeight(a):
    trees = []
    people = []
    for i in range(len(a)):
        if a[i] == -1:
            trees.append(i)
        else:
            people.append(a[i])
    people.sort()
    new = []
    for i in range(len(a)):
        if i in trees:
            new.append(-1)
        else:
            new.append(people[0])
            people.pop(0)
    return new



# You have a string s that consists of English letters, punctuation marks,
# whitespace characters, and brackets. It is guaranteed that the parentheses
# in s form a regular bracket sequence.

# Your task is to reverse the strings contained in each pair of matching
# parentheses, starting from the innermost pair. The results string should not
# contain any parentheses.

# Example

# For string s = "a(bc)de", the output should be
# reverseParentheses(s) = "acbde".

def reverseParentheses(s):
   f1=0
   f2=0
   for i in range(len(s)):
      if f1 != 0 and f2 != 0:
         break
      if s[i] == "(":
         f1 = i
      elif s[i] == ")":
         f2 = i
   if s.find("(") == -1:
      return s
   else:
      return reverseParentheses(s[:f1] + s[f1+1:f2:][::-1] + s[f2+1:])
