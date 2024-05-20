import streamlit as st
import functions as f

todos_list = f.get_todos()   # gets to-dos from archive todos.txt


def add_todo():
    """
    Updates todos file based on new inputs
    """
    # access widget's value according to its key (checkbox, input box, etc)
    added_todo = st.session_state['new_todo'] + '\n'

    if added_todo:
        added_todo = added_todo.capitalize()
        todos_list.append(added_todo)
        f.update_file(todos_list)


# gui setup (header)
st.title('Todo List App')
st.subheader('Welcome!')
st.text('Start being productive right now!')

# adds one checkbox for each to-do
for todo in todos_list:
    st.checkbox(todo, key=todo)  # creates custom key for each to-do
    if st.session_state[todo]:
        todos_list.remove(todo)
        f.update_file(todos_list)
        del st.session_state[todo]
        st.experimental_rerun()

# on_change: action to be executed when user enters a prompt
st.text_input(label='.', placeholder='Add a new todo...', key=f'new_todo', on_change=add_todo, label_visibility='hidden')
st.session_state
