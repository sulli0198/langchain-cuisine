import os
from dotenv import load_dotenv 
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # or "gemini-1.5-pro" for more capable model
    google_api_key=gemini_api_key,
    temperature=0.6
)

name = llm.invoke("I want to open a restaurant for italian food. Suggest a fancy name for this, keep the answer short.")
print(name.content)  # Note: .content to get the text