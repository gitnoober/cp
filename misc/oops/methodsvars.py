class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def msg(self):  # instance method because it accesses unique values of the class
        print(self.name, self.marks)

    @classmethod
    def convert(cls, name, marks):
        return cls(name, marks * 100)

    @staticmethod
    def get_age(age):
        if age < 17:
            print("Baccha")
        else:
            print("Bara Baccha")


s1 = Student("sia", 10)
s2 = Student.convert("pri", 89)
s2.msg()
print(s2)

"""
cls - needs to passed (class method)
staticmethod - doesn't have any special first parameter to be passed
self - first parameter to be passed in instance methods
decorator- it's a function that takes another function as it's argument and returns yet another function (useful in modification of the existing source code)
"""


"""
first class objects - can be used or passed as arguments
# Python program to illustrate functions
# can be treated as objects
"""


def shout(text):
    return text.upper()


print(shout("Hello"))

yell = shout

print(yell("Hello"))


"""
# Python program to illustrate functions
# can be passed as arguments to other functions
"""


def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)


greet(shout)
greet(whisper)


"""
Actual usage
"""


# @gfg_decorator
# def hello_decorator():
#     print("Gfg")


"""Above code is equivalent to -

def hello_decorator():
    print("Gfg")

hello_decorator = gfg_decorator(hello_decorator)"""


"""
Property decorator
Python program to illustrate the use of
@property decorator
"""


# Creating class
class Celsius:

    # Defining init method with its parameter
    def __init__(self, temp=0):
        self._temperature = temp

    # @property decorator
    @property
    # Getter method
    def temp(self):

        # Prints the assigned temperature value
        print("The value of the temperature is: ")
        return self._temperature

    # Setter method
    @temp.setter
    def temp(self, val):

        # If temperature is less than -273 than a value
        # error is thrown
        if val < -273:
            raise ValueError("It is a value error.")

        # Prints this if the value of the temperature is set
        print("The value of the tempereture is set.")
        self._temperature = val


# Creating object for the stated class
cel = Celsius()

# Setting the temperature value
cel.temp = -174  # this will just set the temperature to the passed value

# Prints the temperature that is set
print(cel.temp)  # this will acess the getter method

# Setting the temperature value to -300
# which is not possible so, an error is
# thrown
# cel.temp = -300 # this will raise an error for obvious reasons
