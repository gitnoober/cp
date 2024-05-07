import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def main():
    n = int(input())
    a = list(map(int, input().split()))
    ok2, sfmx, start = [False] * (200010), [], 0
    for idx, i in enumerate(a[::-1]):
        ok2[i] = True
        while ok2[start]:
            start += 1
        sfmx.append(start)

    b, i, sfmx, ok1 = [], 0, sfmx[::-1], [False] * 200010
    while i < n:
        max_mex = sfmx[i]
        start, ii = 0, i
        while i < n:
            ok1[a[i]] = True
            while ok1[start]:
                start += 1
            i += 1
            if start == max_mex:
                break
        while ii < i:
            ok1[a[ii]] = False
            ii += 1
        b.append(start)
    print(len(b), "\n", *b)


tc = int(input())
while tc:
    tc -= 1
    main()
# how couild I miss this the maximum till now will the mex of the suffix
