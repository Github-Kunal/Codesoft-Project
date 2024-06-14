# Initialize an empty list to store tasks
tasks = []

while True:
  # Print the menu options
  print("\nTo-Do List:")
  print("1. Add Task")
  print("2. Show Tasks")
  print("3. Mark Task Done")
  print("4. Exit")

  # Get user input
  choice = input("Enter your choice (1-4): ")

  # Handle user choices
  if choice == '1':
    # Add a new task
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")
  elif choice == '2':
    # Show all tasks
    if tasks:
      print("\nTasks:")
      for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")
    else:
      print("No tasks added yet.")
  elif choice == '3':
    # Mark a task done
    if tasks:
      print("\nTasks:")
      for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")
      task_index = int(input("Enter the number of the task to mark done: ")) - 1
      if 0 <= task_index < len(tasks):
        tasks[task_index] = f"[DONE] {tasks[task_index]}"
        print("Task marked as done!")
      else:
        print("Invalid task number.")
    else:
      print("No tasks to mark done.")
  elif choice == '4':
    # Exit the program
    print("Exiting...")
    break
  else:
    # Handle invalid input
    print("Invalid choice. Please enter a number between 1 and 4.")
