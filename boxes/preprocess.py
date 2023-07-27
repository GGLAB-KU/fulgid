import hashlib
import json
import os
import re
from settings import Settings


def get_number_operations(text):
    move_operations = len(re.findall(r"\bMove\b", text))
    remove_operations = len(re.findall(r"\bRemove\b", text))
    put_operations = len(re.findall(r"\bPut\b", text))

    operations = {
        "Move": move_operations,
        "Remove": remove_operations,
        "Put": put_operations
    }

    total_operations = sum(operations.values())
    operations["Total"] = total_operations

    return operations


def hash_sentence(text, length=10):
    full_hash = hashlib.sha256(text.encode()).hexdigest()
    return full_hash[:length]


dataset_path = os.path.join(Settings.boxes_dataset_path, "test-subsample-states-t5.jsonl")
aggregated_data = {}
BOX_NUMBER = 7
INDEX = 0

with open(dataset_path, 'r') as f:
    lines = f.readlines()

for i in range(0, len(lines), BOX_NUMBER):
    group = lines[i:i + BOX_NUMBER]  # Get the next 7 lines (or fewer if not enough left)
    items = [json.loads(line) for line in group]  # Parse the JSON objects from the lines

    final_states = {}
    remaining_text = ""

    for item in items:
        sample_id = item['sample_id']

        # Formatted content to be appended
        sentence = item['sentence']
        pattern = r'\s*[^.]*\.$'

        # To get the last sentence
        match = re.findall(pattern, sentence, flags=re.DOTALL)
        last_sentence = match[-1].strip() if match else 'No match'
        remaining_text = re.sub(pattern, '', sentence, flags=re.DOTALL)

        # Initialize an empty OrderedDict to store the parsed box states
        match = re.match(r'Box (\d) contains (.+)\.', last_sentence)
        if match:
            box_number = match.group(1)
            box_contents = match.group(2).split(' and ')
            # Convert the set into a list
            box_contents = sorted(list(set(box_contents)))
            # Add to the parsed box states
            final_states['Box ' + box_number] = box_contents

    # Add the parsed box states to the aggregated data
    aggregated_data[INDEX] = {
        'sentence_hash': hash_sentence(remaining_text),
        'sentence': remaining_text,
        'sample_id': items[0]['sample_id'],
        'numops': get_number_operations(remaining_text),
        'final_states': final_states
    }
    INDEX += 1

dataset_path = os.path.join(Settings.boxes_dataset_path, "aggregated_data.jsonl")

with open(dataset_path, 'w') as outfile:
    for sample_id, data in aggregated_data.items():
        json.dump(data, outfile)
        outfile.write('\n')
