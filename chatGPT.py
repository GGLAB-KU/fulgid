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
            "role": "system",
            "content": "Hello world"
        }
    ]
)

# print the chat completion
print(chat_completion.choices[0].message.content)
