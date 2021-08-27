import os
import sys
import time
import itertools as it
import random
osi, oso = '/home/priyanshu/Documents/cp/input.txt', '/home/priyanshu/Documents/cp/output.txt'
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
    # print('choco' * 100000)

    t = 1000
    print(t)
    g = 1
    for _ in range(t):
        print(g)
        g += 1

    #     n = random.randint(1, 100000)
    #     m = random.randint(1, n + 1000)
    #     print(n, m)
    #     for i in range(m):
    #         a = random.randint(1, n)
    #         b = random.randint(1, n)
    #         print(a, b)


if __name__ == '__main__':
    gaurd()
