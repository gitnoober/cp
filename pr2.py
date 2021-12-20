
import sys
import pprint
import logging
from logging import getLogger

def input(): return sys.stdin.readline().rstrip("\r\n")


logging.basicConfig(format="%(message)s", level=logging.WARNING,)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)


def debug(msg, *args):
    logger.info(f'{msg}={pprint.pformat(args)}')

# 30 MINUTES ATLEAST !!!!

###################################################################################################################

# def make_pretty(func):  # takes in a function as an argument

#     def inner(n):  # adds some functionality to the furction
#         arr = func(n)
#         new_arr = [i * i for i in arr]
#         return new_arr

#     return inner  # returns the function


def smart_divide(func):

    def inner(a, b):
        if b == 0:
            print("Not possible")
            return

        print(func(a, b))

    return inner


@smart_divide
def divide(a, b):
    return a / b


# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object

    temperature = property(get_temperature, set_temperature)


human = Celsius(37)

# print(human.temperature)

# print(human.to_fahrenheit())

# human.temperature = -300
