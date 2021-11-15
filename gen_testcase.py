import os
import sys
import time
import itertools as it
import random
osi, oso = '/home/ps/Documents/cp/input.txt', '/home/ps/Documents/cp/output.txt'
if os.path.exists(osi):
    # sys.stdin = open(osi, 'r')
    sys.stdout = open(osi, 'w')


# Function to return the next
# random number
def getNum(v):

    # Size of the vector
    n = len(v)

    # Generate a random number within
    # the index range
    index = random.randint(0, n - 1)

    # Get random number from the vector
    num = v[index]

    # Remove the number from the vector
    v[index], v[n - 1] = v[n - 1], v[index]
    v.pop()

    # Return the removed number
    return num

# Function to generate n non-repeating
# random numbers
def generateRandom(n):

    v = [0] * n

    # Fill the vector with the values
    # 1, 2, 3, ..., n
    for i in range(n):
        v[i] = i + 1

    # While vector has elements get a
    # random number from the vector
    # and print it
    # ans = []
    while (len(v)):
        print(getNum(v), end=" ")
        # ans.append(getNum(v) % 2)
    # return ans


def showallsubsequences(n, s):
    N = 1 << n
    cc = []
    for i in range(N):
        t = []
        for j in range(n):
            if i & (1 << j):
                t.append(s[j])
        cc.append(t)
    return cc


def gaurd():
    tc = 100
    # print(tc)
    n = 5
    s = 'abcdefghijklmnopqrstuvwxyz'
    while tc:
        tc -= 1
        ss = []
        for i in range(n):
            ss.append(random.randint(-10, 10))

        print(*ss)


if __name__ == '__main__':
    gaurd()
