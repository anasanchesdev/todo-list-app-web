import streamlit as st
import functions as f

todos = f.get_todos()   # gets to-dos from archive todos.txt


def add_todo():
    """
    Updates todos file based on new inputs
    """
    added_todo = st.session_state['new_todo'] + '\n' # access widget's value according to its key (checkbox, input box, etc)
    if added_todo:
        added_todo = added_todo.capitalize()
        todos.append(added_todo)
        f.update_file(todos)


# gui setup (header)
st.title('Todo List App')
st.subheader('Welcome!')
st.text('Start being productive right now!')

# adds one checkbox for each to-do
for index, todo in enumerate(todos):
    st.checkbox(todo, key=f'{index}')

# on_change: action to be executed when user enters a prompt
st.text_input(label='.', placeholder='Add a new todo...', key=f'new_todo', on_change=add_todo, label_visibility='hidden')
print(st.session_state['new_todo'])
