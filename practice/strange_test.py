import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


# lOOKOUT FOR THE EDGE CASES

for _ in range(int(input())):
    a, b = map(int, input().split())
    B, ans, cnt = b, min(b - a, (a | b) - b + 1), 0
    while True:
        if a | b == b:
            cnt += 1
            break
        cnt += 1
        b += 1
    ans, cnt = min(ans, cnt), 0
    for i in range(a, B + 2):
        if i | B == B:
            cnt += 1
            break
        cnt += 1
    ans = min(ans, cnt)
    print(ans)
