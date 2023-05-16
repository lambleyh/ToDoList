import functions as fn
import PySimpleGUI as sg

label = sg.Text("Enter a to-do item: ")
input_box = sg.InputText(tooltip = "Enter to-do", key="todo", do_not_clear=False)
add_botton = sg.Button("Add")

window = sg.Window('To-Do App',
                    layout=[[label], [input_box, add_botton]], 
                    font=('Calibri',10))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = fn.read_todos()
            todos.append(values['todo'] + '\n')
            fn.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.close()