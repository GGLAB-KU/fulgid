import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

# list models
models = openai.Model.list()

# print the first model's id

# create a chat completion
chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": """Erosion by the ocean:
1. Wind creates waves in the ocean. 
2. The waves wash onto the beaches. 
3. The waves hit rocks on the beach. 
4. Tiny parts of the rock break off.
5. The rocks become smaller.

I have the above procedural text. Create a python code for it which has different classes for the participants and their relationship with each other.
"""
        }
    ]
)

# print the chat completion
print(chat_completion.choices[0].message.content)
