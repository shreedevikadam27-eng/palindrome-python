import sys

string = sys.argv[1] if len(sys.argv) > 1 else "madam"

reverse = string[::-1]

print("Given string:", string)

if string == reverse:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")