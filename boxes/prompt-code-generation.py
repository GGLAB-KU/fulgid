import json
import pathlib
import time
import argparse

from base import openai, SLEEP_SECONDS


def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def process_dataset(
        aggregated_data_path,
        code_representation_base_path,
        sample_prompt_path,
        sample_code_path,
        new_sample_prompt_path,
        engine,
        temperature,
):
    sample_prompt = read_file_content(sample_prompt_path)
    sample_code = read_file_content(sample_code_path)
    new_sample_prompt = read_file_content(new_sample_prompt_path)

    with open(aggregated_data_path, 'r') as aggregated_boxes_file:
        aggregated_boxes = aggregated_boxes_file.readlines()

    for json_str in aggregated_boxes:
        data = json.loads(json_str)
        sentence = data['sentence']
        sentence_hash = data['sentence_hash']

        code_representation_path = pathlib.Path(f"{code_representation_base_path}/{sentence_hash}.py")

        if not code_representation_path.is_file():
            try:
                response = openai.ChatCompletion.create(
                    model=engine,
                    messages=[
                        {"role": "user", "content": sample_prompt},
                        {"role": "assistant", "content": sample_code},
                        {"role": "user", "content": new_sample_prompt.format(sentence=sentence)},
                    ],
                    temperature=temperature,
                )
                output = response['choices'][0]['message']['content']

                with open(code_representation_path, 'w') as f:
                    f.write(output)
                print(sentence_hash, "finished")
            except openai.error.OpenAIError as e:
                print(e)
                print("sleeping")
                time.sleep(SLEEP_SECONDS)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate code representation using OpenAI.')
    parser.add_argument('--aggregated_data_path', type=str, required=True, help='Path to the input aggregated data.')
    parser.add_argument('--code_representation_base_path', type=str, required=True,
                        help='Base path for code representations.')
    parser.add_argument('--sample_prompt_path', type=str, required=True,
                        help='Path to the file containing the example text for OpenAI model.')
    parser.add_argument('--sample_code_path', type=str, required=True,
                        help='Path to the file containing the example code corresponding to the given example text.')
    parser.add_argument('--new_sample_prompt_path', type=str, required=True,
                        help='Path to the file containing the template for new examples.')
    parser.add_argument('--engine', type=str, default="gpt-3.5-turbo", help='OpenAI engine to use.')
    parser.add_argument('--temperature', type=float, default=0, help='Temperature setting for OpenAI model.')

    args = parser.parse_args()

    process_dataset(
        args.aggregated_data_path,
        args.code_representation_base_path,
        args.sample_prompt_path,
        args.sample_code_path,
        args.new_sample_prompt_path,
        args.engine,
        args.temperature,
    )
