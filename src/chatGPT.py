import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

# list models
models = openai.Model.list()

# print the first model's id
prompt_template = "I have the above procedural text. Create a python code for it which has different classes for the participants and their relationship with each other."

# Opening JSON file
json_file = open('../datasets/wiqa-dataset-v2-october-2019/train.jsonl', 'r')
json_list = list(json_file)

for json_str in json_list:
    result = json.loads(json_str)
    print(f"result: {result}")
    print(isinstance(result, dict))
    stem = result['question']['stem']
    para_steps = result['question']['para_steps']
    joined_procedure = "\n".join(para_steps)
    print(joined_procedure)
    # create a chat completion
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": joined_procedure + prompt_template
            }
        ]
    )

    # print the chat completion
    print(chat_completion.choices[0].message.content)
