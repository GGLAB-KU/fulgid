import argparse
import glob
import json
import pathlib

from utils import convert_str_to_dict, execute_code, plotting, print_metrics, update_counts, load_text

ENGINE = "gpt-3.5-turbo"


def get_sentence_hash_from_path(text):
    filename = pathlib.Path(text).name  # get the filename
    name_without_extension = filename.split('.')[0]  # split by '.' and take the first element
    return name_without_extension


def evaluate_dataset(dataset_path, method, output_base_path):
    data_dict = {}

    with open(dataset_path, 'r') as aggregated_boxes_file:
        for json_str in aggregated_boxes_file:
            data = json.loads(json_str)
            sentence_hash = data['sentence_hash']

            # Create a deep copy of the data dictionary without the sentence_hash
            data_without_hash = dict(data)
            del data_without_hash['sentence_hash']

            data_dict[sentence_hash] = data_without_hash

    tp_count, fp_count, fn_count = {}, {}, {}

    def do_evaluate(box_data, result, tp_count, fp_count, fn_count):
        final_states = box_data.get('final_states')
        operations_num = box_data['numops']['Total']

        if operations_num not in tp_count:
            tp_count[operations_num], fp_count[operations_num], fn_count[operations_num] = 0, 0, 0
        update_counts(final_states, result, tp_count, fp_count, fn_count, operations_num)

    if method == 'Code':
        output_path_list = glob.glob(f"{output_base_path}/*.py")
        for output_path in output_path_list:
            sentence_hash = get_sentence_hash_from_path(output_path)
            output_data = execute_code(output_path)
            output = convert_str_to_dict(output_data) if 'Traceback' not in output_data else {}
            do_evaluate(data_dict.get(sentence_hash), output, tp_count, fp_count, fn_count)

    elif method == 'Plaintext':
        output_path_list = glob.glob(f"{output_base_path}/*.json")
        for output_path in output_path_list:
            sentence_hash = get_sentence_hash_from_path(output_path)
            with open(output_path, 'r') as out_file:
                output = json.loads(out_file.read())
                do_evaluate(data_dict.get(sentence_hash), output, tp_count, fp_count, fn_count)

    elif method == 'Code+Execution':
        output_path_list = glob.glob(f"{output_base_path}/*.txt")
        for output_path in output_path_list:
            sentence_hash = get_sentence_hash_from_path(output_path)
            with open(output_path, 'r') as out_file:
                output = load_text(out_file.read())
                do_evaluate(data_dict.get(sentence_hash), output, tp_count, fp_count, fn_count)

    ac_map = {
        operations_num: tp / (tp + fp + fn)
        for operations_num, tp, fp, fn in
        zip(tp_count.keys(), tp_count.values(), fp_count.values(), fn_count.values())
    }

    return ac_map, tp_count, fp_count, fn_count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process datasets.')
    parser.add_argument('--dataset_path', type=str, help='Path to the dataset.',
                        default='datasets/original_aggregated_data.jsonl')
    parser.add_argument('--method', type=str, choices=['Code', 'Plaintext', 'Code+Execution'],
                        help='Processing method.', default='Plaintext')
    parser.add_argument('--output_base_path', type=str, help='Base path for prediction outputs.',
                        default='results/original-boxes-dataset/plaintext/gpt-3.5-turbo')

    args = parser.parse_args()

    # Derive the dataset name from the dataset_path
    dataset_filename = pathlib.Path(args.dataset_path).stem  # Get filename without extension
    dataset_name_parts = dataset_filename.split('_')
    dataset_name = ' '.join([part.capitalize() for part in dataset_name_parts])

    accuracy_map, tp, fp, fn = evaluate_dataset(args.dataset_path, args.method, args.output_base_path)

    # Plot and print metrics
    print_metrics(f"{args.method}", dataset_name, tp, fp, fn)
    plotting(accuracy_map, f"{args.method}", dataset_name)
