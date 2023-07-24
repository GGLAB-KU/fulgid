import os
import json
from pathlib import Path

from dotenv import load_dotenv
import openai

from settings import Settings

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ENGINE = "text-davinci-003"

MAX_TOKENS = 4097
TEMPERATURE = 0.3

openai.api_key = OPENAI_API_KEY

example_0 = """Box 0 contains the bomb and the boot, Box 1 contains nothing, Box 2 contains nothing, Box 3 contains the rose and the tissue, Box 4 contains the jacket, Box 5 contains the fish and the painting, Box 6 contains the cross. Put the machine into Box 3. Remove the painting from Box 5. Remove the fish from Box 5. Move the machine and the rose from Box 3 to Box 4. Move the cross from Box 6 to Box 1. Move the cross from Box 1 to Box 3. Move the cross from Box 3 to Box 6. Move the cross from Box 6 to Box 0. Put the bell and the bottle into Box 3.

convert above text to a simple python code:"""

new_example_template = """{sentence}

convert above text to a simple python code similar to previous one:"""


def process_dataset():
    aggregated_data_path = os.path.join(Settings.boxes_dataset_path, "aggregated_data.jsonl")
    aggregated_boxes_file = open(aggregated_data_path, 'r')
    aggregated_boxes = list(aggregated_boxes_file)

    code_example_path = os.path.join(Settings.boxes_dataset_path, "sample.py")
    code_example_file = open(code_example_path, 'r')
    example_code = code_example_file.read()

    for json_str in aggregated_boxes[Settings.sample_range]:
        data = json.loads(json_str)
        sentence = data['sentence']
        sample_id = data['sample_id']
        sentence_hash = data['sentence_hash']

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": example_0},
                {"role": "assistant", "content": example_code},
                {"role": "user", "content": new_example_template.format(sentence=sentence)},
            ],
            temperature=0,
        )
        output = response['choices'][0]['message']['content']
        code_representation_path = Path(Settings.boxes_code_path.format(engine=ENGINE, hash=sentence_hash))

        with open(code_representation_path, 'w') as f:
            f.write(output)
        print(sample_id, "finished")


process_dataset()
