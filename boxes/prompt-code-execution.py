import os
import pathlib
import openai
import time

ENGINE = "gpt-3.5-turbo"
TEMPERATURE = 0

current_dir = pathlib.Path(__file__).parent.resolve()
output_dir = os.path.join(current_dir, "code_output")
boxes_code_path = os.path.join(current_dir, "code/{engine}".format(engine=ENGINE))


def ask_model_to_execute_the_code():
    example_code = open(os.path.join(current_dir, "sample1.py"), 'r')
    answer_output = open(os.path.join(current_dir, "sample1_answer.txt"), 'r')
    example = example_code.read()
    answer = answer_output.read()

    for code_hash in os.listdir(boxes_code_path):
        code_representation_path = pathlib.Path(os.path.join(boxes_code_path, "{filename}".format(filename=code_hash)))
        if code_representation_path.is_file():
            sentence_hash = code_hash[:-3] + ".txt"
            output_path = pathlib.Path(os.path.join(output_dir, sentence_hash))
            if not output_path.is_file():
                code_prompt_file = open(code_representation_path, 'r')
                prompt_code = code_prompt_file.read()

                try:
                    response = openai.ChatCompletion.create(
                        model=ENGINE,
                        messages=[
                            {"role": "user", "content": example},
                            {"role": "assistant", "content": answer},
                            {"role": "user", "content": prompt_code},
                        ],
                        temperature=TEMPERATURE,
                    )
                    output = response['choices'][0]['message']['content']

                    with open(output_path, 'w') as d:
                        d.write(output)
                    print(code_hash, "finished")
                except openai.error.RateLimitError:
                    print("sleeping")
                    time.sleep(20)


ask_model_to_execute_the_code()
