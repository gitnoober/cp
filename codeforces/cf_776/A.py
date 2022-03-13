for _ in range(int(input())):
    s = input()
    c = input()

    def func():
        for i, e in enumerate(s, start=0):
            if i % 2 == 0 and e == c:
                print("YES")
                return
        print("NO")
        return

    func()
