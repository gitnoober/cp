mul = 1
arr = [mul]
for i in range(2, 100):
    mul *= i
    if mul > 10**12:
        break
    arr.append(mul)
mul = 2
for i in range(64):
    mul *= 2
    arr.append(mul)
arr.sort()


for _ in range(int(input())):
    n = int(input())
