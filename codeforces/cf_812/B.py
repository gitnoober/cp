# lOOKOUT FOR THE EDGE CASES


def sol():
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    cnt = 0
    while i < n:
        prev = a[i]
        while i < n and a[i] >= prev:
            prev = a[i]
            i += 1
        while i < n and a[i] <= prev:
            prev = a[i]
            i += 1
        cnt += 1

    # print(cnt)
    if cnt == 1:
        print("YES")
    else:
        print("NO")


tc = int(input())
while tc:
    sol()
    tc -= 1
