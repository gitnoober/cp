
# import sys
# import pprint
# import logging
# from logging import getLogger

# def input(): return sys.stdin.readline().rstrip("\r\n")


# logging.basicConfig(format="%(message)s", level=logging.WARNING,)
# logger = getLogger(__name__)
# logger.setLevel(logging.INFO)


# def debug(msg, *args):
#     logger.info(f'{msg}={pprint.pformat(args)}')

# # 30 MINUTES ATLEAST !!!!

# ###################################################################################################################


# def solve():
#     pass


# if __name__ == '__main__':
#     multi = False
#     t = 1

#     def inp(): return map(int, input().split())

#     if multi:
#         t = int(input())

#     while t:
#         t -= 1
#         solve()


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def msg(self):  # instance method because it accesses unique values of the class
        print(self.name, self.marks)

    @classmethod
    def convert(cls, name, marks):
        return cls(name, marks * 100)


s1 = Student("sia", 10)
s2 = Student.convert("pri", 89)
s2.msg()
print(s2)
