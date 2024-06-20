from langchain_community.llms import ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

embeddings = OllamaEmbeddings(model='mxbai-embed-large')
#db = Chroma.from_documents(texts[:5], embeddings)
model = ollama.Ollama(model='gemma:2b',temperature=0.5)

prompt = ChatPromptTemplate.from_template(
    """
you are an helpful ai assistant that helps people with their queries.

    """

)


import streamlit as st

message = st.chat_input("Enter your message")
# choice = st.multiselect("Select an option", ["Option 1", "Option 2", "Option 3"])
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = ""
if message:
     st.chat_message('user').write(message)
     st.chat_message('ai').write(model(message))

    # st.session_state['conversation'] += "User: " + message + "\n"
    
    # # Generate response from the model
    # response = model(message)
    
    # # Append AI response to the conversation
    # st.session_state['conversation'] += "AI: " + response + "\n"
    
    # # Display the whole conversation
    # st.text(st.session_state['conversation'])   


with st.sidebar:
    st.title("Hello, Streamlit!")
    file = st.file_uploader(label='upload file  ',type=['pdf','txt'])
