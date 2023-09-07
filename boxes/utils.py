import re
import subprocess

from matplotlib import pyplot as plt
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score


def convert_str_to_dict(input_str):
    dict_result = {}
    # split the string into lines
    lines = input_str.split("\n")

    # go through each line
    for line in lines:
        # if line is not empty
        if line:
            # split line into key and value using partition which returns a tuple (head, sep, tail)
            key_str, _, value_str = line.partition(": ")

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


def plotting(accuracy_dict, title, dataset_name):
    # Prepare data for the plot
    operations_nums = sorted(accuracy_dict.keys())
    accuracies = [accuracy_dict[num] for num in operations_nums]

    # Create a plot
    plt.figure(figsize=(10, 6))
    plt.plot(operations_nums, accuracies, marker='o')

    # Add labels and title
    plt.xlabel('operations_num')
    plt.ylabel('Accuracy')
    plt.title(dataset_name + " with " + title, fontsize=10)  # Subtitle, with smaller font size

    # Show grid
    plt.grid(True)

    # Show the plot
    plt.tight_layout()
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


def print_metrics(title, dataset_name, tp_count, fp_count, fn_count):
    y_true = ['true_positive'] * sum(tp_count.values()) + ['false_positive'] * sum(fp_count.values()) + [
        'false_negative'] * sum(fn_count.values())
    y_pred = ['true_positive'] * sum(tp_count.values()) + ['true_positive'] * sum(fp_count.values()) + [
        'false_positive'] * sum(fn_count.values())

    precision = precision_score(
        y_true, y_pred, average='weighted',
        labels=['true_positive', 'false_positive', 'false_negative'], zero_division=0
    )
    recall = recall_score(
        y_true, y_pred, average='weighted',
        labels=['true_positive', 'false_positive', 'false_negative'], zero_division=0
    )
    f1 = f1_score(
        y_true, y_pred, average='weighted', labels=['true_positive', 'false_positive', 'false_negative'],
        zero_division=0
    )
    accuracy = accuracy_score(y_true, y_pred)
    print(f".................... {dataset_name} ....................")
    print(f".................... {title} ....................")
    print(f"Precision: {precision * 100:.2f}%")
    print(f"Recall: {recall * 100:.2f}%")
    print(f"F1 Score: {f1 * 100:.2f}%")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print("\n")


def update_counts(final_states, result, tp_count, fp_count, fn_count, operations_num):
    true_positives, false_positives, false_negatives = calculate_metrics(final_states, result)
    tp_count[operations_num] += true_positives
    fp_count[operations_num] += false_positives
    fn_count[operations_num] += false_negatives


def load_text(text):
    pattern = r"Box (\d+): \[([^\]]+)\]"

    matches = re.findall(pattern, text)

    result = {}

    for match in matches:
        box_number, items_str = match
        items = [item.strip().strip("'") for item in items_str.split(',')]
        result[f"Box {box_number}"] = [f"the {item}" for item in items]
    return result


operations = ["Put", "Move", "Remove", "Empty", "Replace", "Swap"]
content_items = [
    "apple", "book", "candle", "pen", "hat",
    "shoe", "shirt", "car", "cup", "laptop",
    "keyboard", "phone", "chair", "table", "watch",
    "bracelet", "guitar", "drum", "piano", "flute",
    "glasses", "spoon", "fork", "plate", "bowl",
    "blanket", "pillow", "lamp", "toothbrush", "toothpaste",
    "soap", "shampoo", "towel", "mirror", "bag",
    "wallet", "coin", "note", "headphone", "speaker",
    "basket", "vase", "flower", "grass", "tree",
    "leaf", "branch", "butterfly", "bird", "cat",
    "dog", "horse", "cow", "elephant", "tiger",
    "lion", "bear", "fish", "shark", "dolphin",
    "octopus", "starfish", "coral", "seaweed", "rock",
    "mountain", "river", "ocean", "beach", "desert",
    "forest", "jungle", "island", "cloud", "rain",
    "snow", "storm", "thunder", "lightning", "sun",
    "moon", "star", "planet", "comet", "meteor",
    "rocket", "ship", "boat", "submarine", "plane",
    "train", "bus", "truck", "bicycle", "motorcycle",
    "helmet", "glove", "scarf", "umbrella", "key",
    "lock", "clock", "battery", "magnet", "wire",
    "camera", "telescope", "microscope", "needle", "thread",
    "button", "zipper", "belt", "tie", "sock",
    "boot", "sandals", "shorts", "skirt", "dress",
    "jacket", "coat", "swimsuit", "ring", "necklace",
    "earring", "crown", "mask", "wig", "perfume",
    "makeup", "lipstick", "brush", "comb", "polish",
    "toy", "doll", "puzzle", "game", "card",
    "dice", "console", "controller", "charger", "usb",
    "tape", "shelf", "frame", "paint", "sculpture",
    "pot", "pan", "oven", "fridge", "freezer",
    "toaster", "microwave", "blender", "mixer", "grinder",
    "whistle", "horn", "bell", "harmonica", "violin",
    "scissors", "pants", "shoes", "gloves", "razor"
]
