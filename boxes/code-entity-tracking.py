import os
import json
import re
from pathlib import Path

from dotenv import load_dotenv
import openai

from settings import Settings

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ENGINE = "text-davinci-003"

MAX_TOKENS = 4097
TEMPERATURE = 0.3
BOXES_CODE_PATH = '../boxes/code/{engine}/{ques_id}.py'

openai.api_key = OPENAI_API_KEY

example_0 = """Box 0 contains the bomb and the boot, Box 1 contains nothing, Box 2 contains nothing, Box 3 contains the rose and the tissue, Box 4 contains the jacket, Box 5 contains the fish and the painting, Box 6 contains the cross. Put the machine into Box 3. Remove the painting from Box 5. Remove the fish from Box 5. Move the machine and the rose from Box 3 to Box 4. Move the cross from Box 6 to Box 1. Move the cross from Box 1 to Box 3. Move the cross from Box 3 to Box 6. Move the cross from Box 6 to Box 0. Put the bell and the bottle into Box 3.

convert above text to a simple python code:"""

new_example_template = """{sentence}

convert above text to a simple python code similar to previous one:"""


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

    code_example_path = os.path.join(Settings.boxes_dataset, "sample.py")
    code_example_file = open(code_example_path, 'r')

    total_true_positives = 0
    total_false_positives = 0
    total_false_negatives = 0

    for json_str in aggregated_boxes[31:37]:
        data = json.loads(json_str)
        sentence = data['sentence']
        final_states = data['final_states']

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": example_0},
                {"role": "assistant", "content": code_example_file.read()},
                {"role": "user", "content": new_example_template.format(sentence=sentence)},
            ],
            temperature=0,
        )
        output = response['choices'][0]['message']['content']
        code_base_representation_path = Path(CODE_BASE_PATH.format(engine=MODEL_NAME, ques_id=ques_id))

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
