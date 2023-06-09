import streamlit as st
import functions as fn

todos = fn.read_todos()
todos = [item.capitalize() for item in todos]

def add_todo():
    new_todo = st.session_state["new_todo"]
    if new_todo.strip() != "":
        todos.append(new_todo +'\n')
        fn.write_todos(todos)
    st.session_state["new_todo"] = ""

st.title("My Todo App")
st.subheader("Welcome to my to-do list app!")
st.write("Lorem ipsum")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fn.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label = "input", placeholder = "Add a new todo...", 
              label_visibility = "collapsed", on_change = add_todo, 
              key = 'new_todo')

#st.session_state