# lOOKOUT FOR THE EDGE CASES


def sol():
    s = int(input())
    res = []
    cur = 9
    while s:
        x = min(cur, s)
        res.append(x)
        s -= x
        cur -= 1

    # print(res)
    print("".join(map(str, sorted(res))))


tc = int(input())
while tc:
    sol()
    tc -= 1
