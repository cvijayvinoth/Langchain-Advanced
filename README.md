# LangChain Advanced Concepts & GenAI Applications

A practical, hands-on repository covering multi-turn message management, structured prompting, guardrails, LLM evaluation techniques, and an interactive Streamlit web application.

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Repository Structure](#-repository-structure)
- [Core Concepts Covered](#-core-concepts-covered)
- [Application Spotlight (`basic.py`)](#-application-spotlight-basicpy)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Repository Setup](#repository-setup)
  - [Environment Configuration](#environment-configuration)
- [Running the Code](#-running-the-code)
- [License](#-license)

---

## 🔍 Overview

Key concepts and implementations included in this repository:

- **Model Integration & Streaming:** Standardized initialization with `ChatOpenAI` supporting both standard execution (`invoke()`) and token-by-token real-time streaming (`stream()`).
- **Explicit Message Objects:** Structuring conversational state using `SystemMessage`, `HumanMessage`, and `AIMessage`.
- **Prompt Engineering & Formatting:** Enforcing strict output constraints, custom personas, and separating raw response objects from clean text content.
- **Guardrails & Input Safety:** Intercepting invalid or out-of-scope user inputs before sending requests to the language model.
- **LLM Output Evaluation:** Automated evaluation strategies to assess model output quality, compliance, and formatting.
- **Interactive Web UI with Session Memory:** Building a multi-turn recipe generator ("Chef AI Assistant") powered by Streamlit and LangChain's `RunnableWithMessageHistory`.

---

## 📁 Repository Structure

```text
Langchain-Advanced/
├── README.md             # Repository documentation and guide
├── basic.py              # Streamlit Web App: Chef AI Assistant with session memory & streaming
├── breakfast.py          # Structured prompting, persona enforcement & raw vs. clean output
├── chat.py               # Model initialization & real-time response streaming demo
└── messages.py           # Multi-turn conversational memory tracking with Message objects
```

---

## 📚 Core Concepts Covered

1. **Model Integration & Streaming (`chat.py`)**  
   Demonstrates how to initialize `ChatOpenAI` with environment-managed API keys and stream responses in real time using `.stream()`.

2. **Message History & Conversation State (`messages.py`)**  
   Shows how to maintain context across back-and-forth turns by passing an array of `SystemMessage` and `HumanMessage` primitives directly into the LLM chain.

3. **Persona Enforcement & Formatting (`breakfast.py`)**  
   Illustrates setting precise system personas, constraining model outputs to specific structures (e.g., exactly 5 single-line items), and comparing raw `AIMessage` objects with extracted `.content`.

4. **Guardrails (Basic Input Safety)**  
   Covers basic input filtering and defensive prompting techniques to validate user input prior to LLM processing, reducing unnecessary token usage and costs.

5. **LLM Output Evaluation**  
   Explores basic concepts around evaluating LLM responses for factual adherence, formatting rules, and criteria verification.

6. **Stateful GenAI Application (`basic.py`)**  
   Integrates LangChain Expression Language (LCEL), `MessagesPlaceholder`, `InMemoryChatMessageHistory`, and Streamlit into a full-featured recipe app called **Chef AI Assistant**.

---

## 🍳 Application Spotlight (`basic.py`)

The included **Chef AI Assistant** application features:
- **Interactive UI:** Native Streamlit chat elements (`st.chat_message`, `st.chat_input`).
- **Session Memory:** Powered by `RunnableWithMessageHistory` to track context per user session (`streamlit_user_session`).
- **Real-time Streaming:** Renders generated text dynamically chunk-by-chunk using Streamlit placeholders (`st.empty()`).

---

## ⚙️ Getting Started

Follow these step-by-step instructions to set up the repository locally and run the scripts.

### Prerequisites
Ensure you have the following installed on your machine:
- **Python:** Version 3.10 or higher
- **Git:** Installed and configured
- **OpenAI API Key:** Required for model calls (`gpt-4o-mini`)

### Repository Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/cvijayvinoth/Langchain-Advanced.git
   cd Langchain-Advanced
   ```

2. **Create a Virtual Environment:**
   - **On Linux / macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **On Windows:**
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install Dependencies:**
   ```bash
   pip install langchain langchain-openai langchain-core streamlit python-dotenv
   ```

### Environment Configuration

1. **Create a `.env` file in the root directory:**
   ```bash
   touch .env
   ```

2. **Add your OpenAI API Key:**
   ```env
   OPENAI_API_KEY=your_actual_openai_api_key_here
   ```

---

## 🚀 Running the Code

1. **Basic Chat & Real-Time Streaming**  
   Tests `ChatOpenAI` initialization and token streaming in the console:
   ```bash
   python chat.py
   ```

2. **Multi-Turn Conversation Memory**  
   Demonstrates state tracking across multiple dialogue turns using `SystemMessage` and `HumanMessage`:
   ```bash
   python messages.py
   ```

3. **Structured Prompting & Persona Rules**  
   Runs a strict persona test and demonstrates raw object vs. clean text extraction:
   ```bash
   python breakfast.py
   ```

4. **Chef AI Assistant Web Application**  
   Launches the interactive Streamlit chat interface with session history in your default web browser:
   ```bash
   streamlit run basic.py
   ```

---
