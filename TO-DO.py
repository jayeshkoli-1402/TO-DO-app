print("Welcome TO-DO App\n\n".center(100))

#function to show task
def show_tasks():
    try:
        with open("todo.txt", "r") as f:
            lines = f.readlines()
        if not lines:
            print("No tasks found.")
        else:
            for i, line in enumerate(lines, start=1):
                print(f"{i}. {line.strip()}")
    except FileNotFoundError:
        print("No tasks file found.")

mode = int(input("Choose the mode: (0:See tasks, 1:Add task, 2:Remove task, 3:Mark as complete, 4:Exit): "))

#contineus loop until exit is trigrred
while mode != 4:
    # See tasks
    if mode == 0:  
        show_tasks()

    # Add tasks
    elif mode == 1: 
        while True:
            task = input("Enter the task (type 'exit' to go back): ").lower()
            if task == "exit":
                break
            with open("todo.txt", "a") as f:
                f.write(task + "\n") 
            print("Task added successfully.")

    # Remove task
    elif mode == 2:
        show_tasks()
        line_no = input("Enter the number of the task to remove (type 'exit' to go back): ").lower()
        if line_no != "exit":
            try:
                line_no = int(line_no)
                with open("todo.txt", "r") as f:
                    lines = f.readlines()
                if 0 < line_no <= len(lines):
                    del lines[line_no - 1]
                    with open("todo.txt", "w") as f:
                        f.writelines(lines)
                    print("Task removed successfully.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    # Mark as complete
    elif mode == 3:
        show_tasks()
        line_no = input("Enter the number of the task to mark complete (type 'exit' to go back): ").lower()
        if line_no != "exit":
            try:
                line_no = int(line_no)
                with open("todo.txt", "r") as f:
                    lines = f.readlines()
                if 0 < line_no <= len(lines):
                    lines[line_no - 1] = lines[line_no - 1].strip() + " ✅\n"
                    with open("todo.txt", "w") as f:
                        f.writelines(lines)
                    print("Task marked as complete.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    else:
        print("Wrong mode.")

    mode = int(input("\nChoose the mode: (0:See tasks, 1:Add task, 2:Remove task, 3:Mark as complete, 4:Exit): "))