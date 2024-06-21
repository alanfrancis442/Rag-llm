from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains.sequential import SequentialChain
from langchain.chains.llm import LLMChain
from dotenv import load_dotenv
import os

# load_dotenv()

# os.environ["LANGCHAIN_TRACING_V2"] = 'true'
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

llm = Ollama(model="gemma:2b",timeout=1000)

python_prompt = ChatPromptTemplate.from_messages([
        ('system', """You are a good programmer who writes python code. You will write the code based on the give question."""),
          
        ('user', "Question:{question}"),
])

java_prompt = ChatPromptTemplate.from_messages([
        ('system', "you are a good programmer who writes java code. You will convert the given code in other language into java code."),
        ('user', "Code:{question}"),
])

javaScript_prompt = ChatPromptTemplate.from_messages([
        ('system', "you are a good programmer who writes javaScript code. You will convert the given code in other language into javaScript code."),
        ('user', "Code:{question}"),
])

python_chain = LLMChain(llm=llm,prompt=python_prompt,output_key='python_code',output_parser=StrOutputParser())
java_chain = LLMChain(llm=llm,prompt=java_prompt,output_key='java_code',output_parser=StrOutputParser())
javaScript_chain = LLMChain(llm=llm,prompt=javaScript_prompt,output_key='javaScript_code',output_parser=StrOutputParser())

llm_chain = SequentialChain(chains=[python_chain,java_chain,javaScript_chain],
                            input_variables=['question'],
                            output_variables=['python_code','java_code','javaScript_code'],
                            verbose=True)


while True:
    question = input("Enter your question: ")
    response = llm_chain.invoke({'question': question})
    #print(response)
    for key, value in response.items():
        print(f"{key}: {value}")