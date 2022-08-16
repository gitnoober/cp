def sol():
    int(input())
    s = input()
    if (s[0] == "A" and s[-1] == "B") or s == "BA":
        print("No")
    else:
        print("Yes")


tc = 1
while tc:
    sol()
    tc -= 1
