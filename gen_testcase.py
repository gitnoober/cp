import itertools as it
import os
import random
import sys
import time
osi, oso = '/home/ps/Documents/cp/input.txt', '/home/ps/Documents/cp/output.txt'
if os.path.exists(osi):
    # sys.stdin = open(osi, 'r')
    sys.stdout = open(osi, 'w')


def prime_sieve(n):
    """returns a sieve of primes >= 5 and < n"""
    flag = n % 6 == 2
    sieve = bytearray((n // 3 + flag >> 3) + 1)
    for i in range(1, int(n**0.5) // 3 + 1):
        if not (sieve[i >> 3] >> (i & 7)) & 1:
            k = (3 * i + 1) | 1
            for j in range(k * k // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
            for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
    return sieve


def prime_list(n):
    """returns a list of primes <= n"""
    res = []
    if n > 1:
        res.append(2)
    if n > 2:
        res.append(3)
    if n > 4:
        sieve = prime_sieve(n + 1)
        res.extend(3 * i + 1 | 1 for i in range(1, (n + 1) // 3 + (n % 6 == 1))
                   if not (sieve[i >> 3] >> (i & 7)) & 1)
    return res

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
    tc = 1
    # s = 'abcdefghijklmnopqrstuvwxyz'
    xx = []
    while tc:
        tc -= 1
        n = 20
        print(n)
        print('y' + 'z' * (n - 1))


if __name__ == '__main__':
    gaurd()
