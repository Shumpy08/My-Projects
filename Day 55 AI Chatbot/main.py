import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')

genai.configure(
    api_key=API_KEY
)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
instructions = ("In this chat, respond as if you are my friend")
while True:
    question = input("Shumpy: ")
    if question.strip() == "":
        break
    response = chat.send_message(instructions + question)
    print('\n')
    print(f"Gemi: {response.text}")
    print('\n')
    instructions = ''
