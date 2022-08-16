# lOOKOUT FOR THE EDGE CASES
from collections import deque, defaultdict


def sol():
    n = int(input())
    a = list(map(int, input().split()))
    # d = defaultdict(deque)
    # for i in range(n):
    # 	d[a[i]].append(i)
    d = defaultdict(int)
    for i in a:
        d[i] += 1

    need = defaultdict(int)
    cnt = 0
    for i in d:
        if d[i] == 1:
            continue
        need[i] = d[i] - 1
        cnt += 1

    i = 0
    # print(cnt)
    while i < n and cnt > 0:
        need[a[i]] -= 1
        if need[a[i]] == 0:
            cnt -= 1
        # print(need, cnt, need[a[i]])
        i += 1

    print(i)


tc = int(input())
while tc:
    sol()
    tc -= 1
