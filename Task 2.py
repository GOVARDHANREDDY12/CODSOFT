import string
import random

length = int(input("Enter the length of password:- "))

print('''Make choices of which you have to make password:
1. Digits
2. Letters
3. Special symbol
4. Exit''')

charList = ""

while (True):
    choice = int(input("Select your choice"))
    if (choice == 1):

        charList += string.ascii_letters
    elif (choice == 2):

        charList += string.digits
    elif (choice == 3):

        charList += string.punctuation
    elif (choice == 4):
        break
    else:
        print("Please choose a option to form password")

pwd = []

for i in range(length):
    randomcharacter = random.choice(charList)
    pwd.append(randomcharacter)

print("Your password is " + "".join(pwd))
