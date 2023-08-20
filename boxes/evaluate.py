import json
import os
import re
import subprocess
from pathlib import Path
import matplotlib.pyplot as plt

from settings import Settings

ENGINE = "gpt-3.5-turbo"


def convert_str_to_dict(input_str):
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
        return None
    return output.decode()


def plotting(accuracy_dict, title):
    # Prepare data for the plot
    operations_nums = sorted(accuracy_dict.keys())
    accuracies = [accuracy_dict[num] for num in operations_nums]
    # Create a plot
    plt.figure(figsize=(10, 6))
    plt.plot(operations_nums, accuracies, marker='o')
    # Add labels and title
    plt.xlabel('operations_num')
    plt.ylabel('Accuracy')
    plt.title(title)
    # Show grid
    plt.grid(True)
    # Show the plot
    plt.show()


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


def print_metrics(title, tp_count, fp_count, fn_count):
    total_true_positives = sum(tp_count.values())
    total_false_positives = sum(fp_count.values())
    total_false_negatives = sum(fn_count.values())

    precision = total_true_positives / (total_true_positives + total_false_positives)
    recall = total_true_positives / (total_true_positives + total_false_negatives)
    f1_score = 2 * ((precision * recall) / (precision + recall))
    accuracy = total_true_positives / (total_true_positives + total_false_positives + total_false_negatives)

    print(f".................... {title} ....................")
    print(f"Precision: {precision * 100:.2f}%")
    print(f"Recall: {recall * 100:.2f}%")
    print(f"F1 Score: {f1_score * 100:.2f}%")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print("\n")


def update_counts(final_states, result, tp_count, fp_count, fn_count, operations_num):
    true_positives, false_positives, false_negatives = calculate_metrics(final_states, result)
    tp_count[operations_num] += true_positives
    fp_count[operations_num] += false_positives
    fn_count[operations_num] += false_negatives


def process_dataset_code():
    aggregated_data_path = os.path.join(Settings.boxes_dataset_path, "aggregated_data.jsonl")
    aggregated_boxes_file = open(aggregated_data_path, 'r')
    aggregated_boxes = list(aggregated_boxes_file)

    tp_count = {}  # true positives count for each operations_num
    fp_count = {}  # false positives count for each operations_num
    fn_count = {}  # false negatives count for each operations_num

    for json_str in aggregated_boxes[Settings.sample_range]:
        data = json.loads(json_str)
        final_states = data['final_states']
        sentence_hash = data['sentence_hash']
        operations_num = data['numops']['Total']

        # Initialize counts for this operations_num if not done yet
        if operations_num not in tp_count:
            tp_count[operations_num] = 0
            fp_count[operations_num] = 0
            fn_count[operations_num] = 0

        code_output_path = Path(Settings.boxes_code_path.format(engine=ENGINE, hash=sentence_hash))
        code_output = execute_code(code_output_path)
        if 'Traceback' not in code_output:
            code_dict_output = convert_str_to_dict(code_output)
        else:
            print("sentence_hash:", sentence_hash, "operations_num: ", operations_num)
            code_dict_output = {}

        update_counts(final_states, code_dict_output, tp_count, fp_count, fn_count, operations_num)

    accuracy_code = {}
    for operations_num in tp_count:
        accuracy_code[operations_num] = tp_count[operations_num] / (
                tp_count[operations_num] + fp_count[operations_num] + fn_count[operations_num])

    return accuracy_code, tp_count, fp_count, fn_count


def process_dataset_simple():
    aggregated_data_path = os.path.join(Settings.boxes_dataset_path, "aggregated_data.jsonl")
    aggregated_boxes_file = open(aggregated_data_path, 'r')
    aggregated_boxes = list(aggregated_boxes_file)

    tp_count = {}  # true positives count for each operations_num
    fp_count = {}  # false positives count for each operations_num
    fn_count = {}  # false negatives count for each operations_num

    for json_str in aggregated_boxes[Settings.sample_range]:
        data = json.loads(json_str)
        final_states = data['final_states']
        sentence_hash = data['sentence_hash']
        operations_num = data['numops']['Total']

        # Initialize counts for this operations_num if not done yet
        if operations_num not in tp_count:
            tp_count[operations_num] = 0
            fp_count[operations_num] = 0
            fn_count[operations_num] = 0

        simple_output_path = Path(Settings.boxes_simple_path.format(engine=ENGINE, hash=sentence_hash))
        simple_prompt_file = open(simple_output_path, 'r')
        simple_output = json.loads(simple_prompt_file.read())

        update_counts(final_states, simple_output, tp_count, fp_count, fn_count, operations_num)

    accuracy_code = {}
    for operations_num in tp_count:
        accuracy_code[operations_num] = tp_count[operations_num] / (
                tp_count[operations_num] + fp_count[operations_num] + fn_count[operations_num])

    return accuracy_code, tp_count, fp_count, fn_count


def process_dataset_simple_execution():
    aggregated_data_path = os.path.join(Settings.boxes_dataset_path, "aggregated_data.jsonl")
    aggregated_boxes_file = open(aggregated_data_path, 'r')
    aggregated_boxes = list(aggregated_boxes_file)

    def load_text(text):
        pattern = r"Box (\d+): \[([^\]]+)\]"

        matches = re.findall(pattern, text)

        result = {}

        for match in matches:
            box_number, items_str = match
            items = [item.strip().strip("'") for item in items_str.split(',')]
            result[f"Box {box_number}"] = [f"the {item}" for item in items]
        return result

    tp_count = {}  # true positives count for each operations_num
    fp_count = {}  # false positives count for each operations_num
    fn_count = {}  # false negatives count for each operations_num

    for json_str in aggregated_boxes[Settings.sample_range]:
        data = json.loads(json_str)
        final_states = data['final_states']
        sentence_hash = data['sentence_hash']
        operations_num = data['numops']['Total']

        # Initialize counts for this operations_num if not done yet
        if operations_num not in tp_count:
            tp_count[operations_num] = 0
            fp_count[operations_num] = 0
            fn_count[operations_num] = 0

        simple_output_path = Path(Settings.boxes_execute_path.format(engine=ENGINE, hash=sentence_hash))
        simple_prompt_file = open(simple_output_path, 'r')
        simple_output = load_text(simple_prompt_file.read())

        update_counts(final_states, simple_output, tp_count, fp_count, fn_count, operations_num)

    accuracy_code = {}
    for operations_num in tp_count:
        accuracy_code[operations_num] = tp_count[operations_num] / (
                tp_count[operations_num] + fp_count[operations_num] + fn_count[operations_num])

    return accuracy_code, tp_count, fp_count, fn_count


# Call the process_dataset functions
# accuracy_map_code, tp_code, fp_code, fn_code = process_dataset_code()
accuracy_map_simple, tp_simple, fp_simple, fn_simple = process_dataset_simple()
# accuracy_map_simple_exc, tp_simple_exc, fp_simple_exc, fn_simple_exc = process_dataset_simple_execution()

# Plot the charts
# plotting(accuracy_map_code, "Python Code Representation")
plotting(accuracy_map_simple, "Text Prompting")
# plotting(accuracy_map_simple_exc, "Simple Execution")

# Print the metrics
print_metrics("Text Prompting", tp_simple, fp_simple, fn_simple)
# print_metrics("Python Code Representation", tp_code, fp_code, fn_code)
# print_metrics("Simple Execution", tp_simple_exc, fp_simple_exc, fn_simple_exc)
