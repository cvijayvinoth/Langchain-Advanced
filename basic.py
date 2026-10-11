import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

# 1. Page Configuration
st.set_page_config(
    page_title="Chef AI - Recipe Assistant", page_icon="🍳", layout="centered"
)

st.title("🍳 Chef AI Assistant")
st.caption("Tell me an ingredient, and I'll whip up a quick 3-step recipe!")

# 2. Environment Variables & API Key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error(
        "OpenAI API Key not found. Please set `OPENAI_API_KEY` in your `.env` file."
    )
    st.stop()

# 3. Initialize In-Memory Store & LangChain Chain in Session State
if "store" not in st.session_state:
    st.session_state.store = {}


def get_session_history(session_id: str):
    if session_id not in st.session_state.store:
        st.session_state.store[session_id] = InMemoryChatMessageHistory()
    return st.session_state.store[session_id]


@st.cache_resource
def get_langchain_chain():
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key, temperature=0.7)

    prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert chef. When given an ingredient or prompt, create a quick and easy 3-step recipe or follow-up recommendation.",
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "I want to cook something quick using {ingredient}"),
        ]
    )

    chain = prompt_template | llm | StrOutputParser()

    return RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="ingredient",
        history_messages_key="chat_history",
    )


chain_with_history = get_langchain_chain()
session_config = {"configurable": {"session_id": "streamlit_user_session"}}

# 4. Initialize and Display Chat History UI
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Handle User Input & Streaming Output
if user_input := st.chat_input("Enter an ingredient (e.g., chicken, eggs, mushrooms)..."):
    # Render user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Render assistant streaming response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        # Stream response from LangChain
        for chunk in chain_with_history.stream(
            {"ingredient": user_input}, config=session_config
        ):
            full_response += chunk
            response_placeholder.markdown(full_response + "▌")

        response_placeholder.markdown(full_response)

    # Save assistant response to UI chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": full_response}
    )