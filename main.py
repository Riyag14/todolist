# Initialize an empty todo list
todo_list = []

# Function to add a task to the todo list
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

# Function to remove a task from the todo list
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed from the list.")
    else:
        print(f"Task '{task}' not found in the list.")

# Function to display the current todo list
def display_todo_list():
    if todo_list:
        print("Todo List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")
    else:
        print("Todo List is empty.")

# Main program loop
while True:
    print("\nTodo List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Todo List")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "3":
        display_todo_list()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
