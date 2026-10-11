from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from os import getenv
from dotenv import load_dotenv
load_dotenv()

# Initializing the language model with GPT-4o-mini and setting up the API key from environment variables
llm = ChatOpenAI(model="gpt-4o-mini", api_key=getenv("OPENAI_API_KEY"), temperature=0)

# Making an initial query to the language model
#response = llm.invoke([
#    SystemMessage(content="You are a helpful assistant. Keep answers very short."),
#    HumanMessage(content="What is variable in python?")
#])
#print(response.content)

## Holding conversation with the model using messages
conversation = [
    SystemMessage(content="You are a helpful assistant. Keep answers very short."),
    HumanMessage(content="My Name is Vijay.")
]
response = llm.invoke(conversation)
print(response.content)

conversation.append(HumanMessage(content="What is my name?"))
response = llm.invoke(conversation)
print(response.content) 