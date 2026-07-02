def reverseString(s):
    reverseS = ""
    for char in s:
        reverseS = char + reverseS
    return reverseS


print(reverseString("Hello, World!"))
