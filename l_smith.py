from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains.sequential import SequentialChain
from langchain.chains.llm import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = 'true'
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

llm = Ollama(model="gemma:2b",timeout=1000)

propmpt = ChatPromptTemplate.from_messages([
        ('system', "you are a helpful chatbot that helps people with their questions based on the  given context."),
        ('user', "Question:{question}\nContext:{context}"),
])

propmpt = ChatPromptTemplate.from_messages([
        ('system', "you are a helpful chatbot that helps people with their questions"),
        ('user', "Question:{question}"),
])

llm_chain = LLMChain(llm=llm,prompt=propmpt)

while True:
    question = input("Enter your question: ")
    response = llm_chain.invoke({'question': question})
    print(response)