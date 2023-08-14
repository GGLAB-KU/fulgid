import json
import os
import pathlib
import openai
import time

from settings import Settings

ENGINE = "gpt-3.5-turbo"
TEMPERATURE = 0


def ask_model_to_execute_the_code():
    aggregated_data_path = os.path.join(Settings.boxes_dataset_path, "aggregated_data.jsonl")
    aggregated_boxes_file = open(aggregated_data_path, 'r')
    aggregated_boxes = list(aggregated_boxes_file)

    for json_str in aggregated_boxes[Settings.sample_range]:
        data = json.loads(json_str)
        sentence_hash = data['sentence_hash']

        code_representation_path = pathlib.Path(Settings.boxes_code_path.format(engine=ENGINE, hash=sentence_hash))

        output_path = pathlib.Path(Settings.boxes_execute_path.format(engine=ENGINE, hash=sentence_hash))

        if code_representation_path.is_file() and not output_path.is_file():
            code_file = open(code_representation_path, 'r')
            code = code_file.read()
            code_prompt = "Run the following code and print the results:\n\n" + code
            try:
                response = openai.ChatCompletion.create(
                    model=ENGINE,
                    messages=[
                        {"role": "user", "content": code_prompt},
                    ],
                    temperature=TEMPERATURE,
                )
                output = response['choices'][0]['message']['content']

                with open(output_path, 'w') as d:
                    d.write(output)
                print(sentence_hash, "finished")
            except openai.error.OpenAIError:
                print("sleeping")
                time.sleep(20)


ask_model_to_execute_the_code()
