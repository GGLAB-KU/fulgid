import os
import time
import json
from pathlib import Path
from dotenv import load_dotenv
import openai
import tiktoken

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "text-davinci-003"
JSONL_PATH = '../datasets/wiqa-dataset-v2-october-2019/train.jsonl'
RESPONSE_PATH = '../responses/{engine}/{ques_id}.py'
SLEEP_TIME = 60
MAX_TOKENS = 4097

openai.api_key = OPENAI_API_KEY


def generate_prompt(steps):
    prompt_base = "I have a procedural event with the following steps. " \
                  "Create a python code for it which has different classes for" \
                  " the participants and their relationship with each other.\n"
    for step in steps:
        prompt_base += f'- {step}\n'
    return prompt_base


def num_tokens_from_string(string: str, model_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def get_code_representation_from_gpt(steps):
    prompt = generate_prompt(steps)

    num_tokens = num_tokens_from_string(prompt, MODEL_NAME)

    response = openai.Completion.create(
        engine=MODEL_NAME,
        prompt=prompt,
        temperature=0.3,
        max_tokens=MAX_TOKENS - num_tokens,
    )
    return response.choices[0].text.strip()


def process_dataset():
    with open(JSONL_PATH, 'r') as json_file:
        json_list = list(json_file)

    for json_str in json_list:
        data = json.loads(json_str)
        ques_id = data['metadata']['ques_id']
        code_representation_path = Path(RESPONSE_PATH.format(engine=MODEL_NAME, ques_id=ques_id))

        if not code_representation_path.is_file():
            code_representation = get_code_representation_from_gpt(data['question']['para_steps'])
            with open(code_representation_path, 'w') as f:
                f.write(code_representation)
            print(ques_id, "finished")

            # Avoid hitting rate limit
            time.sleep(SLEEP_TIME)


process_dataset()
