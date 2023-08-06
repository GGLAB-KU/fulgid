import json
import os
import pathlib
import subprocess
from pathlib import Path

ENGINE = "gpt-3.5-turbo"
current_dir = pathlib.Path(__file__).parent.resolve()
dataset_path = Path(os.path.join(current_dir, "dataset/dev.jsonl"))
prediction_path = Path(os.path.join(current_dir, "results/simple-predictions.json"))

dataset_items = list(open(dataset_path, 'r'))

items = dataset_items[10:110]


def execute_code(code):
    try:
        proc = subprocess.Popen(['python3', str(code)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, _ = proc.communicate(timeout=3)
    except subprocess.TimeoutExpired:
        proc.kill()
        return None
    return output.decode()


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


def process_dataset_code():
    true_positives = 0
    false_positives = 0
    false_negatives = 0
    total_predictions = 0

    for str_item in items:
        data = json.loads(str_item)
        answer = data['answer']
        sentence = data['sentence']
        option1 = data['option1']
        option2 = data['option2']

        qID = data['qID']

        code_representation_path = Path(
            os.path.join(current_dir, "results/code/{engine}/{hash}.py".format(engine=ENGINE, hash=qID)))
        code_output = execute_code(code_representation_path)

        if 'Traceback' not in code_output:
            predict = code_output.replace("\n", "")
            if option1 == predict:
                predict = '1'
            if option2 == predict:
                predict = '2'
        else:
            print("qID:", qID)
            predict = ""

        total_predictions += 1

        if answer == predict:
            true_positives += 1
        elif predict == "":
            false_negatives += 1
        else:
            false_positives += 1

    accuracy = true_positives / total_predictions
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) != 0 else 0
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) != 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0

    print(f"Code Accuracy: {accuracy * 100:.2f}%")
    print(f"Code Precision: {precision * 100:.2f}%")
    print(f"Code Recall: {recall * 100:.2f}%")
    print(f"Code F1-Score: {f1_score * 100:.2f}%")


def process_dataset_simple():
    true_positives = 0
    false_positives = 0
    false_negatives = 0
    total_predictions = 0
    with open(prediction_path, 'r') as f:
        predictions = json.load(f)

    for str_item in items:
        data = json.loads(str_item)
        answer = data['answer']
        sentence = data['sentence']
        qID = data['qID']
        predict = predictions.get(qID)
        total_predictions += 1

        if answer == predict:
            true_positives += 1
        elif predict == "":
            false_negatives += 1
        else:
            false_positives += 1

    accuracy = true_positives / total_predictions
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) != 0 else 0
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) != 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0

    print(f"Accuracy: {accuracy * 100:.2f}%")
    print(f"Precision: {precision * 100:.2f}%")
    print(f"Recall: {recall * 100:.2f}%")
    print(f"F1-Score: {f1_score * 100:.2f}%")


# Call the process_dataset functions
process_dataset_code()
process_dataset_simple()
