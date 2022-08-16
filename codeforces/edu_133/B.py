# lOOKOUT FOR THE EDGE CASES


def sol():
    n = int(input())
    print(n)
    a = list(range(1, n + 1))
    i = 0
    print(*a)
    while i < n - 1:
        a[i], a[i + 1] = a[i + 1], a[i]
        i += 1
        print(*a)


tc = int(input())
while tc:
    sol()
    tc -= 1
