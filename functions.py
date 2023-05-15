def listprint(list):
    """ Print all of the items in a list in separate lines with numbering. 
    """
    for i, item in enumerate(list):
        # new_todos = [item.strip('\n) for item in todos]
        print(f"{i+1}. {item.capitalize()}".strip('\n'))


if __name__ == "__main__":
    print("Hello")