import os
import json
import re
from pathlib import Path

from dotenv import load_dotenv
import openai
import tiktoken

from settings import Settings

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ENGINE = "text-davinci-003"

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
        desc = desc.replace(".", "")
        # Extract the box number and the items
        match = re.match(r'(\d+) contains (.*)', desc)

        if match:
            box_num = 'Box ' + match.group(1)
            items = [item.strip() for item in re.split(', and | and |, ', match.group(2))]
            box_dict[box_num] = items

    return box_dict


def calculate_metrics(final_states, result):
    true_positives = 0
    false_positives = 0
    false_negatives = 0

    for box, items in final_states.items():
        result_items = result.get(box, [])

        # remove trailing '.' if exists
        result_items = [item.rstrip('.') for item in result_items]

        # Convert lists to sets to make comparison easier
        items_set = set(items)
        result_set = set(result_items)

        true_positives += len(items_set & result_set)
        false_positives += len(result_set - items_set)
        false_negatives += len(items_set - result_set)

    return true_positives, false_positives, false_negatives


def process_dataset():
    aggregated_data_path = os.path.join(Settings.boxes_dataset_path, "aggregated_data.jsonl")
    aggregated_boxes_file = open(aggregated_data_path, 'r')
    aggregated_boxes = list(aggregated_boxes_file)

    prompt_path = os.path.join(Settings.boxes_dataset_path, "prompt_incontext.txt")
    prompt_file = open(prompt_path, 'r')
    prompt_template = prompt_file.read()

    for json_str in aggregated_boxes[100:105]:
        data = json.loads(json_str)
        sentence = data['sentence']
        sample_id = data['sample_id']
        sentence_hash = data['sentence_hash']

        prompt = prompt_template.format(desc=sentence)

        num_tokens = num_tokens_from_string(prompt, ENGINE)
        response = openai.Completion.create(
            engine=ENGINE,
            prompt=prompt,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS - num_tokens,
        )
        output = response.choices[0].text.strip()

        parsed_output = parse_output(output)

        json_parsed_output = json.dumps(parsed_output, indent=4)

        output_path = Path(Settings.boxes_simple_path.format(engine=ENGINE, hash=sentence_hash))

        with open(output_path, 'w') as f:
            f.write(json_parsed_output)
        print(sample_id, "finished")


process_dataset()
