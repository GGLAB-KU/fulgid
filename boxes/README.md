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
datasets/original_aggregated_data.jsonl
```



```shell
python3 prompt-code-execution.py \
--dataset_path datasets/original_aggregated_data.jsonl \
--code_representation_base_path results/original-boxes-dataset/code/gpt-3.5-turbo/ \
--code_execution_base_path results/original-boxes-dataset/code-execution/gpt-3.5-turbo/
```

```shell
python3 prompt-code-generation.py \
--dataset_path datasets/original_aggregated_data.jsonl \
--code_representation_base_path results/original-boxes-dataset/code/gpt-3.5-turbo/ \
--sample_prompt_path datasets/sample1/sample-prompt.txt \
--sample_code_path datasets/sample1/code.py \
--new_sample_prompt_path datasets/sample1/prompt.txt
```


```shell
python3 prompt-plaintext.py \
--dataset_path datasets/original_aggregated_data.jsonl \
--output_base_path results/original-boxes-dataset/plaintext/gpt-3.5-turbo/
```

# Complex dataset commands:

```shell
python3 prompt-plaintext.py \
--dataset_path datasets/complex_aggregated_data.jsonl \
--output_base_path results/complex-boxes-dataset/plaintext/gpt-3.5-turbo/
```


```shell
python3 evaluate.py \
--dataset_path datasets/complex_aggregated_data.jsonl \
--method Plaintext \
--output_base_path results/complex-boxes-dataset/plaintext/gpt-3.5-turbo/
```


```shell
python3 evaluate.py \
--dataset_path datasets/complex_aggregated_data.jsonl \
--method Code \
--output_base_path results/complex-boxes-dataset/code/gpt-3.5-turbo/
```

```shell
python3 evaluate.py \
--dataset_path datasets/complex_aggregated_data.jsonl \
--method Code \
--output_base_path results/complex-boxes-dataset/zero-shot-code/gpt-3.5-turbo/
```


```shell
python3 prompt-code-generation.py \
--dataset_path datasets/complex_aggregated_data.jsonl \
--code_representation_base_path results/complex-boxes-dataset/code/gpt-3.5-turbo/ \
--sample_prompt_path datasets/sample2/sample-prompt.txt \
--sample_code_path datasets/sample2/code.py \
--new_sample_prompt_path datasets/sample2/prompt.txt
```

```shell
python3 zero-shot-prompt-code-generation.py \
--dataset_path datasets/complex_aggregated_data.jsonl \
--code_representation_base_path results/complex-boxes-dataset/zero-shot-code/gpt-3.5-turbo/ \
--prompt_path datasets/zero-shot-prompt.txt
```


```shell
python3 prompt-plaintext.py \
--dataset_path datasets/complex_aggregated_data.jsonl \
--output_base_path results/complex-boxes-dataset/plaintext/gpt-4 \
--engine gpt-4
```

```shell
python3 evaluate.py \
--dataset_path datasets/complex_aggregated_data.jsonl \
--method Plaintext \
--output_base_path results/complex-boxes-dataset/plaintext/gpt-4
```
