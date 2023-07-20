def get_toggled_case_string(string: str) -> str:
    lst: list = []
    for index in range(len(string)):
        if string[index].isalpha():
            lst.append(chr(ord(string[index]) ^ 1 << 5))
    return "".join(lst)


try:
    strng = input("Enter a string : ")
    print("The toggled string is : ", get_toggled_case_string(strng))
except ValueError:
    print("Invalid Input, Please enter only a string")