import sys


class TodoApplication:

    def __init__(self):
        self.todoList = []
        self.commands = {
            "add": self.addTask,
            "remove": self.removeTask,
            "list": self.listItems,
            "exit": self.exit,
        }

    def addTask(self):
        taskToAdd = input("Enter a task to complete: ")
        self.todoList.append(taskToAdd)
        print(f"Added {taskToAdd}")

    def removeTask(self):
        taskToRemove = input("Enter a task to remove: ")
        self.todoList.remove(taskToRemove)
        print(f"Removed {taskToRemove}")

    def listItems(self):
        for i in self.todoList:
            print(i)

    def exit(self):
        print("Exiting...")
        sys.exit()


# Instantiating/Begin
start = TodoApplication()

while True:
    action = input("What would you like to do.\nAdd | Remove | List | Exit: ")

    if action in ("Exit", "exit"):
        start.exit()
        break
    else:
        start.commands[action]()
        continue
