import os
import json
import re
import openai
from pathlib import Path
from settings import Settings


ENGINE = "gpt-3.5-turbo"
TEMPERATURE = 0.0

system_msg = 'Given the description after "Description:", write a true statement about all boxes and their contents to the description after "Statement:".'

user1_msg = 'Description: Box 0 contains the car, Box 1 contains the cross, Box 2 contains the bag and the machine, Box 3 contains the paper and the string, Box 4 contains the bill, Box 5 contains the apple and the cash and the glass, Box 6 contains the bottle and the map.'
assistant1_msg = 'Statement: Box 0 contains the car, Box 1 contains the cross, Box 2 contains the bag and the machine, Box 3 contains the paper and the string, Box 4 contains the bill, Box 5 contains the apple and the cash and the glass, Box 6 contains the bottle and the map.'

user2_msg = 'Description: Box 0 contains the car, Box 1 contains the cross, Box 2 contains the bag and the machine, Box 3 contains the paper and the string, Box 4 contains the bill, Box 5 contains the apple and the cash and the glass, Box 6 contains the bottle and the map. Remove the car from Box 0. Remove the paper and the string from Box 3. Put the plane into Box 0. Move the map from Box 6 to Box 2. Remove the bill from Box 4. Put the coat into Box 3.'
assistant2_msg = 'Statement: Box 0 contains the plane, Box 1 contains the cross, Box 2 contains the bag and the machine and the map, Box 3 contains the coat, Box 4 contains nothing, Box 5 contains the apple and the cash and the glass, Box 6 contains the bottle.'


def parse_output(output):
    # Remove the "Statement: " prefix
    text = output.replace("Statement: ", "")

    # Extract the box descriptions without dropping "Box 0"
    box_descs = re.findall(r'Box \d+ contains (?:[^B]*(?:(?=, Box)|$))', text)

    box_dict = {}
    for desc in box_descs:
        desc = desc.replace(".", "")
        # Extract the box number and the items
        match = re.match(r'Box (\d+) contains (.*)', desc)

        if match:
            box_num = 'Box ' + match.group(1)
            items = [item.strip() for item in re.split(', and | and |, ', match.group(2))]
            box_dict[box_num] = items

    return box_dict


def process_dataset():
    dataset_path = os.path.join(Settings.winogrande_dataset_path, "dev.jsonl")
    dataset_file = open(dataset_path, 'r')
    dataset_obj_list = list(dataset_file)

    for json_str in dataset_obj_list[:10]:
        data = json.loads(json_str)
        sentence = data['sentence']
        option1 = data['option1']
        option2 = data['option2']
        answer = data['answer']
        qID = data['qID']
        output_path = Path(Settings.boxes_simple_path.format(engine=ENGINE, hash=sentence_hash))

        if not output_path.is_file():
            response = openai.ChatCompletion.create(
                model=ENGINE,
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": user1_msg},
                    {"role": "assistant", "content": assistant1_msg},
                    {"role": "user", "content": user2_msg},
                    {"role": "assistant", "content": assistant2_msg},
                    {"role": "user", "content": f'Description: {sentence}'},
                ],
                temperature=TEMPERATURE,
            )
            output = response['choices'][0]['message']['content']

            parsed_output = parse_output(output)

            json_parsed_output = json.dumps(parsed_output, indent=4)

            with open(output_path, 'w') as f:
                f.write(json_parsed_output)
            print(sample_id, "finished")


process_dataset()
