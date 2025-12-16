import random
import string

print("1. Numbers\n2. Words\n3. Both")
choice = int(input("Enter your choice: "))
length = int(input("Enter length: "))

letters = list(string.ascii_letters)
numbers = list(string.digits)

password = ""
chars = []

if choice == 1:
    chars = numbers
elif choice == 2:
    chars = letters
elif choice == 3:
    chars = letters + numbers
else:
    print("Invalid choice!")
    exit()

# Simplest method: Direct string concatenation in loop
for i in range(length):
    password += random.choice(chars)

print("\nPassword:", password)
