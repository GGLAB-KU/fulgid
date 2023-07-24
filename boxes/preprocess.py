import json
import os
import re
from collections import OrderedDict
from settings import Settings

dataset_path = os.path.join(Settings.boxes_dataset_path, "test-subsample-states-t5.jsonl")
# Initialize an empty dictionary to store the aggregated data
aggregated_data = {}
BOX_NUMBER = 7
with open(dataset_path, 'r') as f:
    lines = f.readlines()
index = 0
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
    aggregated_data[index] = {
        'sentence': remaining_text,
        'sample_id': items[0]['sample_id'],
        'numops': items[0]['numops'],
        'final_states': final_states
    }
    index += 1


dataset_path = os.path.join(Settings.boxes_dataset_path, "aggregated_data.jsonl")

with open(dataset_path, 'w') as outfile:
    for sample_id, data in aggregated_data.items():
        json.dump(data, outfile)
        outfile.write('\n')

