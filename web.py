import streamlit as st
import functions as f

st.title("Todo List App")
st.subheader("Welcome!")
todos = f.get_todos()

# adds one checkbox for each to-do
for todo in todos:
    st.checkbox(todo)
