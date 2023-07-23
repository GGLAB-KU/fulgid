import os
import json
import re
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
    aggregated_data_path = os.path.join(Settings.boxes_dataset, "aggregated_data.jsonl")
    aggregated_boxes_file = open(aggregated_data_path, 'r')
    aggregated_boxes = list(aggregated_boxes_file)

    prompt_path = os.path.join(Settings.boxes_dataset, "prompt_incontext.txt")
    prompt_file = open(prompt_path, 'r')
    prompt_template = prompt_file.read()

    total_true_positives = 0
    total_false_positives = 0
    total_false_negatives = 0

    for json_str in aggregated_boxes[:5]:
        data = json.loads(json_str)
        sentence = data['sentence']
        final_states = data['final_states']

        prompt = prompt_template.format(desc=sentence)

        num_tokens = num_tokens_from_string(prompt, ENGINE)
        response = openai.Completion.create(
            engine=ENGINE,
            prompt=prompt,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS - num_tokens,
        )
        output = response.choices[0].text.strip()

        result = parse_output(output)

        true_positives, false_positives, false_negatives = calculate_metrics(final_states, result)
        total_true_positives += true_positives
        total_false_positives += false_positives
        total_false_negatives += false_negatives

    precision = total_true_positives / (total_true_positives + total_false_positives)
    recall = total_true_positives / (total_true_positives + total_false_negatives)
    f1_score = 2 * ((precision * recall) / (precision + recall))
    accuracy = total_true_positives / (total_true_positives + total_false_positives + total_false_negatives)

    print(f"Precision: {precision * 100:.2f}%")
    print(f"Recall: {recall * 100:.2f}%")
    print(f"F1 Score: {f1_score * 100:.2f}%")
    print(f"Accuracy: {accuracy * 100:.2f}%")


process_dataset()
