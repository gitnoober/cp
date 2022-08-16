n = int(input())
for _ in range(n):
    arr = [list(map(int, input().split())) for _ in range(2)]
    cntx, cnty = 0, 0
    for i in range(2):
        cntx += sum(arr[i])

    # print(cntx)
    if cntx == 4:
        print(2)
    elif cntx == 0:
        print(0)
    # elif cntx == 1 or cntx == 3 :
    else:
        print(1)
    # else:
    #   if (arr[0][0] == arr[1][1] == 1) or (arr[0][1] == arr[1][0] == 1):
    #       print(1)

    #   # 2 ,3
