import json
import os
import subprocess
from pathlib import Path

from settings import Settings

ENGINE = "text-davinci-003"

failed_code = 0


def convert_str_to_dict(input_str):
    if 'Traceback' in input_str:
        return {}
    dict_result = {}
    # split the string into lines
    lines = input_str.split("\n")

    # go through each line
    for line in lines:
        # if line is not empty
        if line:
            # split line into key and value
            key_str, value_str = line.split(": ")

            # remove unwanted characters from key
            key = key_str.replace("User\n\"", "")

            # split value_str into list items
            value_list_str = value_str.replace("[", "").replace("]", "").replace("'", "").replace("\n", "").split(", ")

            # prefix each item in the list with 'the ' or replace the empty list with ['nothing']
            value_list = ['the ' + item if item else 'nothing' for item in value_list_str] if value_list_str != [
                ''] else ['nothing']

            # add key and value to dictionary
            dict_result[key] = sorted(value_list)

    return dict_result


def execute_code(code):
    try:
        proc = subprocess.Popen(['python3', str(code)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, _ = proc.communicate(timeout=3)
    except subprocess.TimeoutExpired:
        proc.kill()
        global failed_code
        failed_code += 1
        return None
    return output.decode()


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


def create_metrics(total_false_negatives, total_false_positives, total_true_positives):
    precision = total_true_positives / (total_true_positives + total_false_positives)
    recall = total_true_positives / (total_true_positives + total_false_negatives)
    f1_score = 2 * ((precision * recall) / (precision + recall))
    accuracy = total_true_positives / (total_true_positives + total_false_positives + total_false_negatives)
    print(f"Precision: {precision * 100:.2f}%")
    print(f"Recall: {recall * 100:.2f}%")
    print(f"F1 Score: {f1_score * 100:.2f}%")
    print(f"Accuracy: {accuracy * 100:.2f}%")


def process_dataset():
    aggregated_data_path = os.path.join(Settings.boxes_dataset_path, "aggregated_data.jsonl")
    aggregated_boxes_file = open(aggregated_data_path, 'r')
    aggregated_boxes = list(aggregated_boxes_file)

    total_true_positives = 0
    total_false_positives = 0
    total_false_negatives = 0

    total_true_positives_code = 0
    total_false_positives_code = 0
    total_false_negatives_code = 0

    for json_str in aggregated_boxes[Settings.sample_range]:
        data = json.loads(json_str)
        final_states = data['final_states']
        sentence_hash = data['sentence_hash']

        simple_output_path = Path(Settings.boxes_simple_path.format(engine=ENGINE, hash=sentence_hash))
        code_output_path = Path(Settings.boxes_code_path.format(engine=ENGINE, hash=sentence_hash))

        simple_prompt_file = open(simple_output_path, 'r')
        simple_output = json.loads(simple_prompt_file.read())

        code_output = execute_code(code_output_path)
        code_dict_output = convert_str_to_dict(code_output)

        true_positives, false_positives, false_negatives = calculate_metrics(final_states, simple_output)

        total_true_positives += true_positives
        total_false_positives += false_positives
        total_false_negatives += false_negatives

        true_positives, false_positives, false_negatives = calculate_metrics(final_states, code_dict_output)

        total_true_positives_code += true_positives
        total_false_positives_code += false_positives
        total_false_negatives_code += false_negatives

    print(".................... Simple Prompt ....................")

    create_metrics(total_false_negatives, total_false_positives, total_true_positives)

    print(".................... Code Representation ....................")

    create_metrics(total_false_negatives_code, total_false_positives_code, total_true_positives_code)


process_dataset()
