tc = int(input())
while tc:
    tc -= 1
    st = input()
    n = len(st)

    pref = [0]

    s = ans = 0
    for i in st:
        pref.append(pref[-1] + (1 if i == "1" else 0))

    i = 1
    while (i**2) + i <= n:
        jump = (i**2) + i
        for j in range(0, n - jump + 1):
            if pref[j + jump] - pref[j] == i:
                ans += 1
        i += 1
    print(ans)
