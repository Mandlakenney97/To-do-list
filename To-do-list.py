def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        f.write("\n".join(tasks))

def main():
    tasks = load_tasks()
    while True:
        print("\n1. View  2. Add  3. Remove  4. Quit")
        choice = input("Choose: ")
        if choice == "1":
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
        elif choice == "2":
            tasks.append(input("New task: "))
            save_tasks(tasks)
        elif choice == "3":
            idx = int(input("Task number to remove: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
                save_tasks(tasks)
        elif choice == "4":
            break

main()
