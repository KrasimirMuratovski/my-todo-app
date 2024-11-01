import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
	todo=st.session_state["new_todo"]+'\n'
	#session_state is like a dict
	todos.append(todo)
	functions.write_todos(todos)

st.title("My ToDo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")


for todo in todos:
	checkbox = st.checkbox(todo, key=todo)
	if checkbox==True:
		todos.remove(todo)
		functions.write_todos(todos)
		del st.session_state[todo]
		st.rerun()

st.text_input(label = "", placeholder="Add a new todo.....",
			  on_change=add_todo, key = "new_todo")

st.session_state