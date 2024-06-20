import streamlit as st

doc = st.chat_input("Enter your message")
# choice = st.multiselect("Select an option", ["Option 1", "Option 2", "Option 3"])
st.chat_message('user').write('user input')
st.chat_message('ai').write('ai response')
st.chat_message('user').write('user input')
st.chat_message('ai').write('loream ipsum')
if doc:
    st.write(doc)


with st.sidebar:
    st.title("Hello, Streamlit!")
    file = st.file_uploader(label='upload file  ',type=['pdf','txt'])