import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


def find(x):
    xcopy = x

    while x != par[x]:
        x = par[x]

    while xcopy != x:
        xcopy, par[xcopy] = par[xcopy], x

    return x


n, k = maps()
a = [*maps()]
par = list(range(n))
c = a.copy()
for __ in range(k):
    x, y = maps()
    x -= 1
    y -= 1
    # x , y = find(x) , find(x)
    x, y = find(x), find(y)

    if c[x] > c[y]:
        par[x] = y
    else:
        par[y] = x
print(sum(c[i] for i in range(n) if par[i] == i))
