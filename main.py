import functions as fn
import time

filename = 'todos.txt'
with open(filename,'r') as file:
    todos = file.readlines()

now = time.strftime("%d.%m.%Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add [item], show, edit [no.], "
                        "remove [no.] or exit: ").strip().lower()

    if user_action.startswith("add"):
        list_item = user_action.removeprefix(user_action.split()[0]).strip()
        todos.append(list_item +'\n')
    elif user_action.startswith("show") or user_action.startswith("display"):
        if len(todos) == 0:
            print("The list is empty!")
        else:
            fn.listprint(todos)
    elif user_action.startswith("edit"):
        try:
            num = user_action.split()[1]
            todos[int(num)-1] = input("Overwriting list item %s: " % todos[
                int(num)-1].strip('\n').upper()) + '\n'
        except ValueError:
            print("Please enter a valid command")
            continue
        except IndexError:
            print("Please choose an item number in the list")

    elif user_action.startswith("remove"):
        try:
            # num = user_action.removeprefix(user_action.split()[0]).strip()
            num = user_action.split()[1]
            removed_todo = todos.pop(int(num) - 1).strip('\n')
            print(f"To do item {removed_todo.upper()} was removed from the list")
        except ValueError:
            print("Please enter a valid command")
            continue
        except IndexError:
            print("Please choose an item number in the list")

    elif user_action.startswith("exit"):
        break
    else:
        print("Please enter a valid command!")

with open(filename,'w') as file:
    file.writelines(todos)

print("See you next time!")