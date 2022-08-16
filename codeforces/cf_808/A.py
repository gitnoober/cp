from math import gcd

N = int(input())
for _ in range(N):
    n = int(input())
    a = list(map(int, input().split()))
    gc = a[0]
    for i in range(1, n):
        gc = gcd(gc, a[i])
    ok = False
    if gc == a[0]:
        ok = True

    print(["NO", "YES"][ok])
