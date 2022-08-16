from collections import defaultdict

N = int(input())
for _ in range(N):
    s = input()
    p = int(input())
    d = defaultdict(list)
    cur = 0
    for idx, i in enumerate(s):
        d[i].append(idx)
        cur += (ord(i) - ord("a")) + 1
    # print(cur)
    nn = len(s)

    for i in "abcdefghijklmnopqrstuvwxyz"[::-1]:
        while cur > p and len(d[i]):
            d[i].pop()
            cur -= (ord(i) - ord("a")) + 1
            nn -= 1

    ans = [None] * len(s)
    for i in d:
        for j in d[i]:
            ans[j] = i
    print("".join([i for i in ans if i]))
