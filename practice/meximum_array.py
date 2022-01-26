import sys
def input(): return sys.stdin.readline().rstrip("\r\n")


def main():
    n = int(input())
    a = list(map(int, input().split()))


tc = int(input())
while tc:
    tc -= 1
    main()
