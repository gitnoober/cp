N = int(input())
for __ in range(N):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    res = ["B" for _ in range(m)]
    idxs = set()
    for i in range(n):

        if res[a[i] - 1] == res[((m + 1) - a[i]) - 1] == "B":
            if a[i] - 1 < ((m + 1) - a[i]) - 1:
                res[a[i] - 1] = "A"
            else:
                res[((m + 1) - a[i]) - 1] = "A"
        elif res[a[i] - 1] == "B":
            res[a[i] - 1] = "A"
        elif res[((m + 1) - a[i]) - 1] == "B":
            res[((m + 1) - a[i]) - 1] = "A"
    print("".join(res))
    # print(sorted(idxs))
