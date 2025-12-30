import random
def game():
    while True:
        comp_choice = random.randint(1, 3)
        print("1. Rock\n2. Paper\n3. Scissors")
        try:
            user_choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Invalid input. Please enter a number (1-3).")
            continue
        if user_choice not in [1, 2, 3]:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue
        if user_choice == 1:
            choice_name = 'Rock'
        elif user_choice == 2:
            choice_name = 'Paper'
        else:
            choice_name = 'Scissors'
        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'Paper'
        else:
            comp_choice_name = 'Scissors'
        if user_choice == comp_choice:
            result = "DRAW"
        elif (user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 1):
            result = "Paper wins"
        elif (user_choice == 1 and comp_choice == 3) or (user_choice == 3 and comp_choice == 1):
            result = "Rock wins"
        else:
            result = "Scissors wins"
        print(f"\nYou chose: {choice_name}")
        print(f"Computer chose: {comp_choice_name}")
        print("Result:", result)
        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break
        else:
            game()
game()