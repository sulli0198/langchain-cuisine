import os
from dotenv import load_dotenv 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    google_api_key=gemini_api_key,
    temperature=0.6
)

def generate_restaurant_name_and_items(cuisine):
    # Create prompt templates
    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Suggest ONE fancy name for this resturant according to its traditions. Return only the name, nothing else."
    )

    prompt_template_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest some menu items for {restaurant_name}. Return it as a comma separated list."
    )

    # Create two separate chains (same as before)
    name_chain = prompt_template_name | llm
    items_chain = prompt_template_items | llm

    # 1. Run first chain to get restaurant name
    name_response = name_chain.invoke({"cuisine": cuisine}) # Use the function input 'cuisine'
    restaurant_name = name_response.content.strip() 

    # 2. Run second chain using the output from first chain
    items_response = items_chain.invoke({"restaurant_name": restaurant_name})
    menu_items = items_response.content.strip()
    
    # 3. Combine results into a single variable (dictionary)
    result_data = {
        "restaurant_name": restaurant_name,
        "menu_items": menu_items
    }
    
    # Optional: Print for debugging/console output
    print(f"Restaurant Name: {restaurant_name}")
    print(f"Menu Items: {menu_items}")
    
    # 4. Return the single variable
    return result_data




