N = int(input())
for _ in range(N):
    n = int(input())
    a = [input() for __ in range(n)]
    d = {}
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    def check(st):
        for j in range(len(st)):
            # print(st[: j + 1], st[j + 1 :], st)
            if st[: j + 1] in d and st[j + 1 :] in d:
                return True
        return False

    ans = []
    for i in a:
        ans.append("1" if check(i) else "0")
    print("".join(ans))
