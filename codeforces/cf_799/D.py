def convert_time(hr, mins, x):
    while x >= 60:
        hr += 1
        hr %= 24
        x -= 60

    while x > 0:
        mins += 1
        if mins == 60:
            hr += 1
            mins = 0

        if hr == 24:
            hr = 0

        x -= 1

    return hr, mins


def format(hr, mins):
    hr, mins = str(hr), str(mins)
    if len(hr) == 1:
        hr = "0" + hr

    if len(mins) == 1:
        mins = "0" + mins
    return hr + mins


def check_pal(st):
    return st == st[::-1]

    # rem = 60 - mins
    # if rem == x :
    # 	hr+=1
    # elif rem > x :
    # 	mins += x
    # else:
    # 	while


# hr, mins = 13, 22
# x = 2
# for j in range(5):
# 	hr, mins = convert_time(hr,mins,x)
# 	print(hr, mins)


for _ in range(int(input())):
    time, x = input().split()
    hr, mins = map(int, time.split(":"))
    x = int(x)
    vis = set()
    cnt = 0
    res = []
    for _ in range(1440):
        # print(hr, mins, "before")
        hr, mins = convert_time(hr, mins, x)

        if (hr, mins) in vis:
            break
        vis.add((hr, mins))
        st = format(hr, mins)
        if check_pal(st):
            cnt += 1
            # res.append(st)
        # print(hr, mins, "after")
    print(cnt)
