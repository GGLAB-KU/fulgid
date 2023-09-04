## Prerequisites
- Python 3.x
- A dataset in JSONL format.

How to Use

## Setting up:
Clone the repository and navigate to the directory containing preprocess.py.

```shell
git clone [Your Repository URL]
cd [Your Repository Name or Directory]
```

## Running the Script:

You can run the preprocessing script using the following command:


```shell
python3 preprocess.py \
datasets/test-subsample-states-t5.jsonl \
datasets/aggregated_data.jsonl
```



```shell
python3 prompt-code-execution.py \
--input_path datasets/aggregated_data.jsonl \
--code_representation_base_path results/original-boxes-dataset/code/gpt-3.5-turbo/ \
--code_execution_base_path results/original-boxes-dataset/code-execution/gpt-3.5-turbo/
```

```shell
python3 prompt-code-generation.py \
--aggregated_data_path datasets/aggregated_data.jsonl \
--code_representation_base_path results/original-boxes-dataset/code/gpt-3.5-turbo/ \
--sample_prompt_path datasets/sample1/sample-prompt.txt \
--sample_code_path datasets/sample1/code.py \
--new_sample_prompt_path datasets/sample1/prompt.txt
```


```shell
python3 prompt-simple.py \
--aggregated_data_path datasets/aggregated_data.jsonl \
--output_base_path results/original-boxes-dataset/simple/gpt-3.5-turbo/
```

```shell
python3 prompt-simple.py \
--aggregated_data_path datasets/complex_aggregated_data.jsonl \
--output_base_path results/complex-boxes-dataset/simple/gpt-3.5-turbo/
```
