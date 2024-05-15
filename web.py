import streamlit as st
import functions as f

st.title('Todo List App')
st.subheader('Welcome!')
st.text('Start being productive right now!')
todos = f.get_todos()

# adds one checkbox for each to-do
for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Add a new todo...')
