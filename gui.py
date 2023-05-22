import functions as fn
import PySimpleGUI as sg

todos = fn.read_todos()
todos = [item.capitalize() for item in todos]

label = sg.Text("Enter a to-do item: ")
input_box = sg.InputText(tooltip = "Enter to-do", key="todo", do_not_clear=False, size=[40,1])
add_button = sg.Button("Add")
list_box = sg.Listbox(values=todos, key="todolist", 
                      enable_events=True, size=[40,10])
edit_button = sg.Button("Edit")
remove_button = sg.Button("Remove")

window = sg.Window('To-Do App',
                    layout=[[sg.Column([[label], [input_box],[list_box]]),
                            sg.Column([[sg.Text("")],[add_button],[edit_button],
                                       [remove_button]],vertical_alignment='top',
                                       element_justification='right')]], 
                    font=('Calibri',10))


while True:
    event, values = window.read()
    match event:
        case "Add":
            if len(values['todo']) > 0:
                todos.append(values['todo'] + '\n')
                fn.write_todos(todos)
                window['todolist'].update(values=todos)
        case "Edit":
            try:
                todo = values['todolist'][0]
                new_todo = values['todo'].capitalize() + '\n'

                index = todos.index(todo)
                todos[index] = new_todo
                fn.write_todos(todos)

                window['todolist'].update(values=todos)
            except IndexError:
                continue
        case "Remove":
            try:
                todo = values['todolist'][0]
                todos.pop(todos.index(todo))

                fn.write_todos(todos)

                window['todolist'].update(values=todos)
                window['todo'].set_focus()
            except IndexError:
                continue
        case "todolist":
            window['todo'].update(value=values['todolist'][0].strip('\n'))
        case sg.WIN_CLOSED:
            break
window.close()