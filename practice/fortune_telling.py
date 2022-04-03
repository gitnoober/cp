for _ in range(int(input())):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    parity = x % 2
    for i in a:
        parity ^= i % 2

    print("Alice" if y % 2 == parity else "Bob")

"""
xoring/adding - incase the parity of the other number is odd, the parity changes else parity stays the same
"""
