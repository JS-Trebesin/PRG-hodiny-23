import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

user_input = input("What kind of joke do you want?")

response = model.generate_content(f"Tell me a joke on the topic of {user_input}")
print(response.text)
