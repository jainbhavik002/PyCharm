tasks = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == "2":
        for t in tasks:
            print("-", t)
    elif choice == "3":
        break
    else:
        print("Invalid option.")