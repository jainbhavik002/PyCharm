import random
import words
name = input("Your name? ")
print("Good luck", name, "you only have 10 attempts for the right guess")

word = random.choice(words.names)
guesses = ''
turns = 10

while turns > 0:
    # Show word with blanks
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("\nYou WIN!")
        print("Word:", word)
        break

    print()
    guess = input("Guess letter: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong!")
        print("Turns left:", turns)

    if turns == 0:
        print("You LOSE!")
        print("Word was:", word)
