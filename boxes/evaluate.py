import json
import os
import subprocess
from pathlib import Path
import matplotlib.pyplot as plt

from settings import Settings

ENGINE = "text-davinci-003"

failed_code = 0


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
        global failed_code
        failed_code += 1
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


def create_metrics(total_false_negatives, total_false_positives, total_true_positives):
    precision = total_true_positives / (total_true_positives + total_false_positives)
    recall = total_true_positives / (total_true_positives + total_false_negatives)
    f1_score = 2 * ((precision * recall) / (precision + recall))
    accuracy = total_true_positives / (total_true_positives + total_false_positives + total_false_negatives)
    print(f"Precision: {precision * 100:.2f}%")
    print(f"Recall: {recall * 100:.2f}%")
    print(f"F1 Score: {f1_score * 100:.2f}%")
    print(f"Accuracy: {accuracy * 100:.2f}%")


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
            print(sentence_hash)
            code_dict_output = {}

        true_positives, false_positives, false_negatives = calculate_metrics(final_states, code_dict_output)

        # Add the counts to the corresponding operations_num
        tp_count[operations_num] += true_positives
        fp_count[operations_num] += false_positives
        fn_count[operations_num] += false_negatives

    accuracy_code = {}
    for operations_num in tp_count:
        accuracy_code[operations_num] = tp_count[operations_num] / (
                tp_count[operations_num] + fp_count[operations_num] + fn_count[operations_num])

    return accuracy_code


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

        true_positives, false_positives, false_negatives = calculate_metrics(final_states, simple_output)

        # Add the counts to the corresponding operations_num
        tp_count[operations_num] += true_positives
        fp_count[operations_num] += false_positives
        fn_count[operations_num] += false_negatives

    accuracy_code = {}
    for operations_num in tp_count:
        accuracy_code[operations_num] = tp_count[operations_num] / (
                tp_count[operations_num] + fp_count[operations_num] + fn_count[operations_num])

    return accuracy_code


# Call the process_dataset function to get the accuracy_code dictionary
# accuracy_map_code = process_dataset_code()
accuracy_map_simple = process_dataset_simple()

# Plot the charts
# plotting(accuracy_map_code, "Python Code Representation")
plotting(accuracy_map_simple, "Simple Prompt")
