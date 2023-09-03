import json
import pathlib
import re
import time
import argparse

from base import openai, SLEEP_SECONDS

system_msg = 'Given the description after "Description:", write a true statement about all boxes and their contents to the description after "Statement:".'

user1_msg = 'Description: Box 0 contains the car, Box 1 contains the cross, Box 2 contains the bag and the machine, Box 3 contains the paper and the string, Box 4 contains the bill, Box 5 contains the apple and the cash and the glass, Box 6 contains the bottle and the map.'
assistant1_msg = 'Statement: Box 0 contains the car, Box 1 contains the cross, Box 2 contains the bag and the machine, Box 3 contains the paper and the string, Box 4 contains the bill, Box 5 contains the apple and the cash and the glass, Box 6 contains the bottle and the map.'

user2_msg = 'Description: Box 0 contains the car, Box 1 contains the cross, Box 2 contains the bag and the machine, Box 3 contains the paper and the string, Box 4 contains the bill, Box 5 contains the apple and the cash and the glass, Box 6 contains the bottle and the map. Remove the car from Box 0. Remove the paper and the string from Box 3. Put the plane into Box 0. Move the map from Box 6 to Box 2. Remove the bill from Box 4. Put the coat into Box 3.'
assistant2_msg = 'Statement: Box 0 contains the plane, Box 1 contains the cross, Box 2 contains the bag and the machine and the map, Box 3 contains the coat, Box 4 contains nothing, Box 5 contains the apple and the cash and the glass, Box 6 contains the bottle.'


def parse_output(output):
    text = output.replace("Statement: ", "")
    box_descs = re.findall(r'Box \d+ contains (?:[^B]*(?:(?=, Box)|$))', text)

    box_dict = {}
    for desc in box_descs:
        desc = desc.replace(".", "")
        match = re.match(r'Box (\d+) contains (.*)', desc)

        if match:
            box_num = 'Box ' + match.group(1)
            items = [item.strip() for item in re.split(', and | and |, ', match.group(2))]
            box_dict[box_num] = items

    return box_dict


def process_dataset(
        aggregated_data_path,
        output_base_path,
        engine,
        temperature,
):
    with open(aggregated_data_path, 'r') as aggregated_boxes_file:
        aggregated_boxes = aggregated_boxes_file.readlines()

    for json_str in aggregated_boxes:
        data = json.loads(json_str)
        sentence = data['sentence']
        sentence_hash = data['sentence_hash']
        output_path = pathlib.Path(f"{output_base_path}/{sentence_hash}.json")

        if not output_path.is_file():
            try:
                response = openai.ChatCompletion.create(
                    model=engine,
                    messages=[
                        {"role": "system", "content": system_msg},
                        {"role": "user", "content": user1_msg},
                        {"role": "assistant", "content": assistant1_msg},
                        {"role": "user", "content": user2_msg},
                        {"role": "assistant", "content": assistant2_msg},
                        {"role": "user", "content": f'Description: {sentence}'},
                    ],
                    temperature=temperature,
                )
                output = response['choices'][0]['message']['content']

                parsed_output = parse_output(output)
                json_parsed_output = json.dumps(parsed_output, indent=4)

                with open(output_path, 'w') as f:
                    f.write(json_parsed_output)
                print(sentence_hash, "finished")
            except openai.error.OpenAIError as e:
                print(e)
                print("sleeping")
                time.sleep(SLEEP_SECONDS)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process the dataset using OpenAI.')
    parser.add_argument('--aggregated_data_path', type=str, required=True, help='Path to the input aggregated data.')
    parser.add_argument('--output_base_path', type=str, required=True, help='Base path for prediction outputs.')
    parser.add_argument('--engine', type=str, default="gpt-3.5-turbo", help='OpenAI engine to use.')
    parser.add_argument('--temperature', type=float, default=0, help='Temperature setting for OpenAI model.')

    args = parser.parse_args()

    process_dataset(
        args.aggregated_data_path,
        args.output_base_path,
        args.engine,
        args.temperature,
    )
