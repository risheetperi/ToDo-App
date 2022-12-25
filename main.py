# from functions import get_todos, write_todos
# MODULES
import functions
import time

greeting = """
Welcome to the To - Do List Program

-RSP

"Hope you have fun!"
"""

print(greeting)
user_prompt = "Type add, show, edit, complete or exit : "

now = time.strftime("%d %b %Y    %H:%M:%S")
print("It is ", now)

while True:

    user_action = input(user_prompt)
    user_action = user_action.strip().lower()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:].title()

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show") or user_action.startswith("display"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item.title()}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()
            todo_to_edit = todos[number].strip('\n').title()
            print(f"Current todo to be edited : {todo_to_edit}")

            new_todo = input("Enter a new todo : ")
            todos[number] = new_todo.title() + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Invalid Command")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1

            todos = functions.get_todos()
            todo_to_remove = todos[number].strip('\n').title()
            print(f"Todo removed from list: {todo_to_remove}")
            todos.pop(number)

            functions.write_todos(todos)

        except IndexError:
            print("No todo with that number")
            continue

    elif 'exit' in user_action:
        break

    else:
        print("Unknown Command")

print("Thank you! Bye!")
