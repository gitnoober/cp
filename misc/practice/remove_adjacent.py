
import logging
import pprint
import sys

from logging import getLogger

def input(): return sys.stdin.readline().rstrip("\r\n")


logging.basicConfig(format="%(message)s", level=logging.WARNING,)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)


def debug(msg, *args):
    logger.info(f'{msg}={pprint.pformat(args)}')

# 30 MINUTES ATLEAST !!!!

###################################################################################################################


def give_new_str(string, i1, i2):
    if string[i1] > string[i2]:
        string.pop(i1)
    else:
        string.pop(i2)
    return string


def recur(s):
    n = len(s)
    for i in range(n):
        if i + 1 < n and s[i] + s[i + 1] in d:
            new_s = give_new_str(s[:], i, i + 1)
            recur(new_s)
        # elif i - 1 >= 0 and s[i - 1] + s[i] in d:
        #     new_s = give_new_str(s[:], i - 1, i)
        #     recur(new_s)
    A.add(''.join(s))


def main():
    n = int(input())
    s = list(input())
    cnt = 0
    i = 0
    for k in range(n):
        temp = []
        mx = 'a'
        idx = -1
        for i in range(len(s)):
            if s[i] > mx and ((i - 1 >= 0 and s[i - 1] + s[i] in d) or (i + 1 < len(s) and s[i] + s[i + 1] in d)):
                mx = s[i]
                idx = i

        if idx != - 1:
            s.pop(idx)

    print(n - len(s))


if __name__ == '__main__':
    A = set()
    d = set()
    _str = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(25):
        d.add(_str[i] + _str[i + 1])
        d.add(_str[i + 1] + _str[i])
    main()
