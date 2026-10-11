from langchain_openai import ChatOpenAI
from os import getenv
from dotenv import load_dotenv
load_dotenv()


llm = ChatOpenAI(model="gpt-4o-mini", api_key=getenv("OPENAI_API_KEY"), temperature=0)

# Get chat response from the model
#response = llm.invoke("What is python ?")
#print(response.content)

# Stream chat response from the model
for chunk in llm.stream("What is python?"):
    print(chunk.content, end="", flush=True)
