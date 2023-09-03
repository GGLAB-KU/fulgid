import argparse
import hashlib
import json
import re


def get_number_operations(text):
    """Count the number of Move, Remove, and Put operations in the text."""
    operations = {
        "Move": len(re.findall(r"\bMove\b", text)),
        "Remove": len(re.findall(r"\bRemove\b", text)),
        "Put": len(re.findall(r"\bPut\b", text))
    }
    operations["Total"] = sum(operations.values())
    return operations


def hash_sentence(text, length=10):
    """Hash a sentence and return a specified number of characters."""
    return hashlib.sha256(text.encode()).hexdigest()[:length]


def process_dataset(input_path, output_path, box_number=7):
    aggregated_data = {}
    index = 0

    with open(input_path, 'r') as f:
        lines = f.readlines()

    for group_start_index in range(0, len(lines), box_number):
        group = lines[group_start_index:group_start_index + box_number]
        items = [json.loads(line) for line in group]

        final_states = {}
        remaining_text = ""

        for item in items:
            sentence = item['sentence']

            # Extract the last sentence from the text.
            match = re.findall(r'\s*[^.]*\.$', sentence, flags=re.DOTALL)
            last_sentence = match[-1].strip() if match else 'No match'
            remaining_text = re.sub(r'\s*[^.]*\.$', '', sentence, flags=re.DOTALL)

            # Extract box number and contents.
            match = re.match(r'Box (\d) contains (.+)\.', last_sentence)
            if match:
                matched_box_number = match.group(1)
                box_contents = sorted(list(set(match.group(2).split(' and '))))
                final_states['Box ' + matched_box_number] = box_contents

        aggregated_data[index] = {
            'sentence_hash': hash_sentence(remaining_text),
            'sentence': remaining_text,
            'sample_id': items[0]['sample_id'],
            'numops': get_number_operations(remaining_text),
            'final_states': final_states
        }
        index += 1

    with open(output_path, 'w') as outfile:
        for data in aggregated_data.values():
            json.dump(data, outfile)
            outfile.write('\n')


if __name__ == '__main__':
    # Setting up command line arguments
    parser = argparse.ArgumentParser(description='Process dataset to aggregate data.')
    parser.add_argument('input_dataset_path', type=str, help='Path to the input dataset.')
    parser.add_argument('output_dataset_path', type=str, help='Path to where the aggregated data should be saved.')

    # Parse the arguments
    args = parser.parse_args()

    # Use the parsed arguments
    process_dataset(args.input_dataset_path, args.output_dataset_path)
