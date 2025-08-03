import streamlit as st
import functions

todos = functions.get_todos()

st.title("To-Do List")
st.subheader("This is a task management application")
st.write("Tasks to be completed:")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")

