import os
import json
import re
from pathlib import Path
from dotenv import load_dotenv
import openai
import tiktoken

from src.settings import Settings

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "text-davinci-003"
CODE_BASE_PATH = '../code-base/{engine}/{ques_id}.py'
CODE_UPDATED_PATH = '../code-updated/{engine}/{ques_id}.py'
CODE_PATH = '../code/{sample_id}.py'

SLEEP_TIME = 100
MAX_TOKENS = 4097
TEMPERATURE = 0.3

openai.api_key = OPENAI_API_KEY


def num_tokens_from_string(string: str, model_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def process_dataset():
    file_path = "few_shot_boxes_nso_exp2_max3/test-subsample-states-t5.jsonl"
    prompt_template_path = "few_shot_boxes_nso_exp2_max3/prompt_incontext.txt"
    dataset_path = os.path.join(Settings.boxes_dataset_v1, file_path)
    json_file = open(dataset_path, 'r')

    prompt_path = os.path.join(Settings.boxes_dataset_v1, prompt_template_path)
    prompt_file = open(prompt_path, 'r')
    prompt_template = prompt_file.read()

    json_list = list(json_file)

    for index in [0,2000]:
        data = json.loads(json_str)
        sentence_masked = data['sentence_masked']
        masked_content = data['masked_content']
        sample_id = data['sample_id']

        pattern = r'\s*[^.]*\.$'
        only_actions = re.sub(pattern, '', sentence_masked, flags=re.DOTALL)
        prompt = prompt_template.format(desc=only_actions)

        # code_representation_path = Path(CODE_PATH.format(sample_id=sample_id))
        # if not code_representation_path.is_file():
        num_tokens = num_tokens_from_string(prompt, MODEL_NAME)
        engine = "text-davinci-003"
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS - num_tokens,
        )
        output = response.choices[0].text.strip()

        for data in json_data:
            # Unmask the sentence
            unmasked_sentence = data["sentence_masked"].replace("<extra_id_0>", data["masked_content"])
            if unmasked_sentence == output:
                print(f"Match found: {unmasked_sentence}")

        # with open(code_representation_path, 'w') as f:
        #     f.write(code_representation)
        print(sample_id, "finished")


process_dataset()
