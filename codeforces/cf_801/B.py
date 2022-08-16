for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2 == 0:
        idx = a.index(min(a))

        if idx % 2 == 0:
            print("Joe")
        else:
            print("Mike")
    else:
        print("Mike")
