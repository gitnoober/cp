import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


def check(s, w, n, x):
    for i in range(n):
        ok = False
        if s[i] == "1" and (
            (i >= x and w[i - x] == "1") or (i + x < n and w[i + x] == "1")
        ):
            ok = True
        else:
            if (i - x < 0 and i + x >= n) or (
                (i - x >= 0 and i + x < n and w[i - x] == w[i + x] == "0")
                or ((i - x >= 0) + (i + x < n)) == 1
                and (i >= x and w[i - x] == "0")
                or (i + x < n and w[i + x] == "0")
            ):
                ok = True

        if not ok:
            return False

    return True


for _ in range(*maps()):
    s = input()
    n = len(s)
    (x,) = maps()
    w = ["1"] * n

    for i in range(n):
        if s[i] == "0" and i >= x:
            w[i - x] = "0"
        if i + x < n and s[i] == "0":
            w[i + x] = "0"

    # print(''.join(w))

    if check(s, w, n, x):
        print("".join(w))
    else:
        print("-1")
