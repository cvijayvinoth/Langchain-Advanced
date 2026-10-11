import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ensure API key is set
if not os.environ.get("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable not set.")

# Step 1: Initialize ChatOpenAI
# Setting temperature=0.0 makes the output deterministic across runs.
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

# Step 2: Define a specific prompt template
# - Defines "healthy": balanced macronutrients (protein, healthy fats, complex carbs).
# - Enforces strict formatting: exactly 5 items, one line each, numbered, no intro/outro text.
prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a nutritionist. Define 'healthy' as balanced in complex carbs, "
            "lean protein, and healthy fats. Provide exactly 5 distinct breakfast ideas. "
            "Formatting rule: Output ONLY a numbered list from 1 to 5, one single line per idea. "
            "Do not include any intro, preamble, notes, or concluding text.",
        ),
        ("user", "Give me 5 healthy breakfast ideas."),
    ]
)

# Step 3: Demonstrate raw message object vs text content
chain = prompt_template | llm

# Print raw invoke output to see the full AIMessage object
print("--- DEMO: RAW invoke() RESULT ---")
raw_response = chain.invoke({})
print(raw_response)
print("\n" + "=" * 50 + "\n")

# Step 4: Extract and print ONLY the string content
print("--- CLEAN OUTPUT (Content Only) ---")
clean_text = raw_response.content
print(clean_text)