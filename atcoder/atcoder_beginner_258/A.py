k = int(input())
hh = 21
mm = 00
dx = k // 60
dy = k % 60
hh += dx
mm += dy
hh, mm = str(hh), str(mm)
if len(mm) == 1:
    mm = "0" + mm
if len(hh) == 1:
    hh = "0" + hh
print(str(hh) + ":" + mm)
