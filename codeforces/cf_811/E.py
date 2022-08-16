# lOOKOUT FOR THE EDGE CASES


def sol():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] % 2:
            a[i] += a[i] % 10
    se = set()
    odd, even, ten, zero = 0, 0, 0, 0
    for i in range(n):
        se.add(a[i])
        if a[i] == 0:
            zero += 1

        if a[i] == 10:
            ten += 1
            continue

        last = a[i] % 10
        if a[i] < 10:
            if a[i] == 6:
                odd += 1
            else:
                even += 1
        else:
            if last in [2, 4, 8]:
                k = int(str(a[i])[-2])
                if k % 2 == 0:
                    even += 1
                else:
                    odd += 1
            elif last == 6:
                k = int(str(a[i])[-2])
                if k % 2 == 0:
                    odd += 1
                else:
                    even += 1
    if zero < n and zero > 0:
        print("No")
        return
    if ten == n or len(se) == 1 or odd == n or even == n:
        print("Yes")
    else:
        print("No")


tc = int(input())
while tc:
    sol()
    tc -= 1
