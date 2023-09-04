import json
import pathlib
import re
import time
import argparse

from base import openai, SLEEP_SECONDS

system_msg = 'Given the description after "Description:", write a true statement about all boxes and their contents to the description after "Statement:".'

user1_msg = 'Description: Box 0 contains the car, Box 1 contains the cross, Box 2 contains the bag and the machine, Box 3 contains the paper and the string, Box 4 contains the bill, Box 5 contains the apple and the cash and the glass, Box 6 contains the bottle and the map.'
assistant1_msg = 'Statement: Box 0 contains the car, Box 1 contains the cross, Box 2 contains the bag and the machine, Box 3 contains the paper and the string, Box 4 contains the bill, Box 5 contains the apple and the cash and the glass, Box 6 contains the bottle and the map.'

user2_msg = 'Description: Box 0 contains the button and the pan, Box 1 contains the necklace and the lipstick and the brush and the comb, Box 2 contains nothing, Box 3 contains the thunder and the battery, Box 4 contains the fish. Remove comb from Box 1. Swap battery in Box 3 with pan in Box 0. Remove necklace from Box 1. Remove lipstick from Box 1. Swap button in Box 0 with pan in Box 3. Swap fish in Box 4 with brush in Box 1. Put oven into Box 1. Replace thunder with wallet in Box 3. Empty Box 0. Put cat into Box 2. Move wallet from Box 3 to Box 0. Move wallet from Box 0 to Box 2. Replace button with lock in Box 3.'
assistant2_msg = 'Statement: Box 0 contains nothing, Box 1 contains the fish and the oven, Box 2 contains the cat and the wallet, Box 3 contains the lock, Box 4 contains the brush.'


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
        dataset_path,
        output_base_path,
        engine,
        temperature,
):
    with open(dataset_path, 'r') as aggregated_boxes_file:
        aggregated_boxes = aggregated_boxes_file.readlines()

    for json_str in aggregated_boxes:
        data = json.loads(json_str)
        sentence = data['sentence']
        sentence_hash = data['sentence_hash']
        output_path = pathlib.Path(f"{output_base_path}/{sentence_hash}.json")

        if not output_path.is_file():
            output_path.parent.mkdir(parents=True, exist_ok=True)
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
    parser.add_argument('--dataset_path', type=str, required=True, help='Path to the input aggregated data.')
    parser.add_argument('--output_base_path', type=str, required=True, help='Base path for prediction outputs.')
    parser.add_argument('--engine', type=str, default="gpt-3.5-turbo", help='OpenAI engine to use.')
    parser.add_argument('--temperature', type=float, default=0, help='Temperature setting for OpenAI model.')

    args = parser.parse_args()

    process_dataset(
        args.dataset_path,
        args.output_base_path,
        args.engine,
        args.temperature,
    )
