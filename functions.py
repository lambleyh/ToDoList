FILEPATH = "todos.txt"


def read_todos(filepath=FILEPATH):
    with open(filepath,'r') as file:
        todos = file.readlines()
        return todos
    
def write_todos(todos, filepath=FILEPATH):
    with open(filepath,'w') as file:
        file.writelines(todos)

def listprint(list):
    """ Print all of the items in a list in separate lines with numbering. 
    """
    for i, item in enumerate(list):
        # new_todos = [item.strip('\n) for item in todos]
        print(f"{i+1}. {item.capitalize()}".strip('\n'))


if __name__ == "__main__":
    print("Hello")