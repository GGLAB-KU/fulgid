import os
import pathlib
import openai
import time

from settings import Settings

ENGINE = "gpt-3.5-turbo"
TEMPERATURE = 0

current_dir = pathlib.Path(__file__).parent.resolve()
output_dir = os.path.join(current_dir, "code_execution")
boxes_code_path = os.path.join(current_dir, "code/{engine}".format(engine=ENGINE))


def ask_model_to_execute_the_code():
    for code_hash in os.listdir(boxes_code_path):
        sentence_hash = code_hash[:-3]

        code_representation_path = pathlib.Path(Settings.boxes_code_path.format(engine=ENGINE, hash=sentence_hash))

        if code_representation_path.is_file():
            text_file = sentence_hash + ".txt"
            output_path = pathlib.Path(os.path.join(output_dir, text_file))
            if not output_path.is_file():
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
                    print(code_hash, "finished")
                except openai.error.OpenAIError:
                    print("sleeping")
                    time.sleep(20)


ask_model_to_execute_the_code()
