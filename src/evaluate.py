import json
import re
from pathlib import Path
import subprocess
import glob

JSONL_PATH = '../datasets/wiqa-dataset-v2-october-2019/train.jsonl'
CODE_BASE_PATH = '../code-base/{engine}/{ques_id}.py'
CODE_UPDATED_PATH = '../code-updated/{engine}/{ques_id}.py'
MODEL_NAME = "text-davinci-003"

result = {
    "all": 0,
    "correct": 0,
    "incorrect": 0,
    "failed": 0,
}


def load_json_data():
    with open(JSONL_PATH, 'r') as json_file:
        json_list = list(json_file)
    return json_list


json_list = load_json_data()


def get_answer_label(ques_id):
    for json_str in json_list:
        data = json.loads(json_str)
        if data['metadata']['ques_id'] == ques_id:
            return data['question']['answer_label']


def execute_code(code):
    try:
        proc = subprocess.Popen(['python3', code], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, _ = proc.communicate(timeout=3)
    except subprocess.TimeoutExpired:
        proc.kill()
        result['failed'] += 1
        return None
    return output.decode()


def validate_output(output, answer_label):
    if output == answer_label:
        result['correct'] += 1
    elif 'Traceback' in output:
        result['failed'] += 1
    elif output != answer_label:
        result['incorrect'] += 1


updated_code = glob.glob(f'../code-updated/{MODEL_NAME}/*.py')

for code in updated_code:
    ques_id = re.search(r'([^/]*)\.py$', code).group(1)
    answer_label = get_answer_label(ques_id)

    code_base_path = Path(CODE_BASE_PATH.format(engine=MODEL_NAME, ques_id=ques_id))
    code_updated_path = Path(CODE_UPDATED_PATH.format(engine=MODEL_NAME, ques_id=ques_id))

    if code_base_path.is_file() and code_updated_path.is_file():
        result['all'] += 1
        output = execute_code(code)
        if output is not None:
            validate_output(output, answer_label)
print(result)
