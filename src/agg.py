import json
import os
import re

from src.settings import Settings

dataset_path = os.path.join(Settings.boxes_dataset, "test-subsample-states-t5.jsonl")

# Initialize an empty dictionary to store the aggregated data
aggregated_data = {}

# Open the JSON Lines file
with open(dataset_path, 'r') as f:
    # Read each line of the file
    for line in f:
        # Parse the JSON object from the line
        item = json.loads(line)

        sample_id= item['sample_id']

        # Formatted content to be appended
        sentence = item['sentence']
        pattern = r'\s*[^.]*\.$'

        # To get the last sentence
        match = re.findall(pattern, sentence, flags=re.DOTALL)
        last_sentence = match[-1].strip() if match else 'No match'

        # Split the final states into separate box states
        box_states = last_sentence.split(', ')

        # Initialize an empty dictionary to store the parsed box states
        parsed_box_states = {}

        # Parse each box state
        for box_state in box_states:
            # Extract the box number and its contents
            match = re.match(r'Box (\d) contains (.+)\.', box_state)
            if match:
                box_number = match.group(1)
                box_contents = match.group(2).split(' and ')
                # Convert the set into a list
                box_contents = list(set(box_contents))
                # Add to the parsed box states
                parsed_box_states['Box ' + box_number] = box_contents

        # To get the remaining text
        remaining_text = re.sub(pattern, '', sentence, flags=re.DOTALL)

        # If the sample_id is already in the aggregated data, update the formatted content
        if item['sample_id'] in aggregated_data:
            for box, items in parsed_box_states.items():
                if box in aggregated_data[item['sample_id']]['final_states']:
                    # Update the list, convert to set for union operation, and convert back to list for JSON compatibility
                    aggregated_data[item['sample_id']]['final_states'][box] = list(set(aggregated_data[item['sample_id']]['final_states'][box]).union(set(items)))
                else:
                    aggregated_data[item['sample_id']]['final_states'][box] = items
        # If the sample_id is not in the aggregated data, add it with the formatted content
        else:
            del item['masked_content']
            del item['sentence_masked']
            aggregated_data[item['sample_id']] = item
            aggregated_data[item['sample_id']]['sentence'] = remaining_text
            aggregated_data[item['sample_id']]['final_states'] = parsed_box_states

dataset_path = os.path.join(Settings.boxes_dataset, "aggregated_data.jsonl")

with open(dataset_path, 'w') as outfile:
    for sample_id, data in aggregated_data.items():
        json.dump(data, outfile)
        outfile.write('\n')
