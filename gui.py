import PySimpleGUI as sg

label = sg.Text("Enter a to-do item: ")
input_box = sg.InputText(tooltip = "Enter to-do")
add_botton = sg.Button("Add")

window = sg.Window('To-Do App', layout=[[label], [input_box, add_botton]])
window.read()
window.close()