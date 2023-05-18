import functions as fn
import PySimpleGUI as sg

todos = fn.read_todos()
todos = [item.capitalize() for item in todos]

label = sg.Text("Enter a to-do item: ")
input_box = sg.InputText(tooltip = "Enter to-do", key="todo", do_not_clear=False)
add_botton = sg.Button("Add")
list_box = sg.Listbox(values=todos, key="todolist", 
                      enable_events=True, size=[40,10])
edit_button = sg.Button("Edit")

window = sg.Window('To-Do App',
                    layout=[[label], [input_box, add_botton],[list_box, edit_button]], 
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
        case "todolist":
            window['todo'].update(value=values['todolist'][0])
        case sg.WIN_CLOSED:
            break
window.close()