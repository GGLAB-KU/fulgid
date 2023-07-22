import os
import json
import re
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


def parse_output(output):
    # Split the output into different box descriptions
    box_descs = re.split(', Box ', output.strip())

    box_dict = {}
    for desc in box_descs:
        # Extract the box number and the items
        match = re.match(r'(\d+) contains (.*)', desc)

        if match:
            box_num = 'Box ' + match.group(1)
            items = [item.strip() for item in re.split(', and | and |, ', match.group(2))]
            box_dict[box_num] = items

    return box_dict


def compare_results(final_states, result):
    total_accuracy = 0
    num_boxes = len(final_states)

    for box, items in final_states.items():
        result_items = result.get(box, [])

        # remove trailing '.' if exists
        result_items = [item.rstrip('.') for item in result_items]

        # Convert lists to sets to make comparison easier
        items_set = set(items)
        result_set = set(result_items)

        # Calculate accuracy as the size of intersection divided by size of union
        box_accuracy = len(items_set & result_set) / len(items_set | result_set)

        total_accuracy += box_accuracy

    # Calculate average accuracy
    accuracy = total_accuracy / num_boxes

    return accuracy


def process_dataset():
    file_path = "few_shot_boxes_nso_exp2_max3/aggregated_data.jsonl"
    prompt_template_path = "few_shot_boxes_nso_exp2_max3/prompt_incontext.txt"
    dataset_path = os.path.join(Settings.boxes_dataset_v1, file_path)
    json_file = open(dataset_path, 'r')

    prompt_path = os.path.join(Settings.boxes_dataset_v1, prompt_template_path)
    prompt_file = open(prompt_path, 'r')
    prompt_template = prompt_file.read()

    json_list = list(json_file)

    for json_str in json_list:
        data = json.loads(json_str)
        sentence = data['sentence']
        final_states = data['final_states']
        sample_id = data['sample_id']

        prompt = prompt_template.format(desc=sentence)

        num_tokens = num_tokens_from_string(prompt, MODEL_NAME)
        engine = "text-davinci-003"
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS - num_tokens,
        )
        output = response.choices[0].text.strip()

        result = parse_output(output)

        accuracy = compare_results(final_states, result)
        print(f"Accuracy: {accuracy * 100:.2f}%")
        print(sample_id, "finished")


process_dataset()
