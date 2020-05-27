#print True if S has alphanumeric char
#print True if S has alphabetical char
#print True if S has digits
#print True if S has lowercase char
#print True if S has uppercase char

def check(s):
    for i in s:
        if any(letter.isalnum() for letter in i):
            print("True")
        if any(letter.isalpha()for letter in i):
            print("True")
        if any(letter.isdigit() for letter in i):
            print("True")
        if any(letter.isupper() for letter in i):
            print("True")
        if any(letter.islower() for letter in i):
            print("True")
        else:
            print("False")
s = input().split()
check(s)
