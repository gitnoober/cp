import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


def search(arr, key):
    l, h = 0, len(arr) - 1
    idx = 1 << 60
    while l <= h:
        m = (l + h) // 2
        if arr[m] <= key:
            l = m + 1
        else:
            idx = m
            h = m - 1
    return idx


for _ in range(*maps()):
    (n,) = maps()
    s = input()
    pos0 = []
    pos1 = []
    tot = 0
    ans = [0] * n
    for idx, i in enumerate(s):
        if i == "0":
            if len(pos1) == 0:
                tot += 1
                pos0.append(tot)
                ans[idx] = tot
            else:
                x = pos1.pop()
                pos0.append(x)
                ans[idx] = x
        else:
            # now i = '1'
            if len(pos0) == 0:
                tot += 1
                pos1.append(tot)
                ans[idx] = tot
            else:
                x = pos0.pop()
                pos1.append(x)
                ans[idx] = x
    print(tot)
    print(*ans)

# basically you're adding a '0' with a subsequence that ends with a '1' (pos1) and then converting to a subsequence ending with a '0'
# given that such a subsequence exists else you create a new subsequence from here on , same logic is applied when concatening
# a '1'.
