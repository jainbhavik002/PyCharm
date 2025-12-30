import random
def game():
  while True:
    number = random.randint(1, 1000)
    print("\nI'm thinking of a number between 1 and 100.")
    print("Type 'q' to quit anytime.")
    while True:
        guess = input("Enter your guess: ")
        if guess.lower() == 'q':
            print("Thanks for playing!")
            quit()
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")
            continue
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Correct! You guessed the number!")
            break
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Goodbye! Thanks for playing.")
        break
    elif play_again == 'y':
      game()
game()