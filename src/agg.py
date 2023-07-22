import json
import os
import re

from src.settings import Settings

file_path = "few_shot_boxes_nso_exp2_max3/test-subsample-states-t5.jsonl"
dataset_path = os.path.join(Settings.boxes_dataset_v1, file_path)

# Initialize an empty dictionary to store the aggregated data
aggregated_data = {}

# Open the JSON Lines file
with open(dataset_path, 'r') as f:
    # Read each line of the file
    for line in f:
        # Parse the JSON object from the line
        item = json.loads(line)

        # Formatted content to be appended
        sentence = item['sentence']
        pattern = r'\s*[^.]*\.$'

        # To get the last sentence
        match = re.findall(pattern, sentence, flags=re.DOTALL)
        last_sentence = match[-1].strip() if match else 'No match'

        # To get the remaining text
        remaining_text = re.sub(pattern, '', sentence, flags=re.DOTALL)

        # If the sample_id is already in the aggregated data, append the formatted content
        if item['sample_id'] in aggregated_data:
            aggregated_data[item['sample_id']]['final_states'] += ', ' + last_sentence
        # If the sample_id is not in the aggregated data, add it with the formatted content
        else:
            del item['masked_content']
            del item['sentence_masked']
            aggregated_data[item['sample_id']] = item
            aggregated_data[item['sample_id']]['sentence'] = remaining_text
            aggregated_data[item['sample_id']]['final_states'] = last_sentence
