import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps(): return [int(i) for i in input().split()]


from math import tan, pi, sin, cos

def C1():

    for _ in range(*maps()):
        n, = maps()
        n *= 2
        print(1 / tan(pi / n))


def C2():

    for _ in range(*maps()):
        n, = maps()
        x = pi / (2 * n)
        y = pi / (4 * n)
        print(cos(y) / sin(x))
