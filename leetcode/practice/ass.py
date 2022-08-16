"""
Problem Statement 1 


file_location = input("Enter source file path: ")
try:
    with open(file_location, "r+") as f:
        characters = 0
        words = 0
        lines = 0
        spaces = 0
        all_lines = f.read()
        for each_line in all_lines:
            characters += 1
            for char in each_line:
                if char == "\n" or char == "\0":
                    lines += 1
                if char == " " or char == "\t" or char == "\n" or char == "\0":
                    words += 1
        if characters > 0:
            words += 1
            lines += 1
        spaces = words - 1
        print(f"Total Words:{words}")
        print(f"Total Spaces:{spaces}")
        print(f"Total Lines:{lines}")


except FileNotFoundError:
    print("Unable to open file.")
"""


"""
Problem Statement 2 


word = input("Enter a word: ")
if len(word) < 2:
    print("Error => Not a word!")
else:
    ok = True
    for each_char in word:
        if ord(each_char) < 65 or ord(each_char) > 122:
            ok = False
            print("Error => Not a word!")
    if ok:
        print("Valid Word!")

"""


"""
Problem Statement 3



def is_keyword(string):
    keywords = {
        "auto",
        "break",
        "case",
        "char",
        "const",
        "continue",
        "default",
        "do",
        "double",
        "else",
        "enum",
        "extern",
        "float",
        "for",
        "goto",
        "if",
        "int",
        "long",
        "register",
        "return",
        "short",
        "signed",
        "sizeof",
        "static",
        "struct",
        "switch",
        "typedef",
        "union",
        "unsigned",
        "void",
        "volatile",
        "while",
    }
    return True if string in keywords else False


file_location = input("Enter source file path: \n")
try:
    with open(file_location, "r+") as f:
        all_lines = f.readlines()
        numbers = 0
        identifier = 0
        for each_line in all_lines:
            each_line = each_line.strip("\n").split()
            for char in each_line:
                if char in ["(", "{", "}", ")", "[", "]", "()", "{}", "[]"]:
                    continue
                char = char.strip(",").strip("\n")
                if char.isalnum():
                    if char.isdigit():
                        print(f"{char} is Number")
                        numbers += 1

                    elif not is_keyword(char):
                        print(f"{char} is identifier")
                        identifier += 1
        print(f"Total Numbers: {numbers}")
        print(f"Total Identifiers: {identifier}")


except FileNotFoundError:
    print("Unable to open file.")
"""


"""
Problem Statement 4





"""
