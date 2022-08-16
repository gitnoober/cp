# lOOKOUT FOR THE EDGE CASES


def sol():
    n, h, m = map(int, input().split())
    A = []
    ok = True
    ansh, ansm = 0, 0
    for i in range(n):
        hh, mm = map(int, input().split())
        if hh == h and mm == m:
            ok = False
        A.append([hh, mm])

    while ok:
        m += 1
        ansm += 1
        if m == 60:
            m = 0
            h += 1

        if ansm == 60:
            ansm = 0
            ansh += 1

        if h == 24:
            h = 0
        # print(h, m, (ansh, ansm))

        if [h, m] in A:
            break
    print(ansh, ansm)


tc = int(input())
while tc:
    sol()
    tc -= 1
