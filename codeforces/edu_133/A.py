# lOOKOUT FOR THE EDGE CASES
from math import ceil


def sol():
    n = int(input())
    if n == 1:
        print(2)
    else:
        x = n // 3
        n -= 3 * x
        print(x + ceil(n / 2))


tc = int(input())
while tc:
    sol()
    tc -= 1
