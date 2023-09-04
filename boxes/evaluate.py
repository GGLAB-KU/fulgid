import argparse
import json
import pathlib

from utils import convert_str_to_dict, execute_code, plotting, print_metrics, update_counts, load_text

ENGINE = "gpt-3.5-turbo"


def evaluate_dataset(dataset_path, method, output_base_path):
    with open(dataset_path, 'r') as aggregated_boxes_file:
        aggregated_boxes = aggregated_boxes_file.readlines()

    tp_count, fp_count, fn_count = {}, {}, {}

    for json_str in aggregated_boxes:
        data = json.loads(json_str)
        final_states = data['final_states']
        sentence_hash = data['sentence_hash']
        operations_num = data['numops']['Total']

        if operations_num not in tp_count:
            tp_count[operations_num], fp_count[operations_num], fn_count[operations_num] = 0, 0, 0

        if method == 'Code':
            output_path = pathlib.Path(f"{output_base_path}/{sentence_hash}.py")
            output_data = execute_code(output_path)
            output = convert_str_to_dict(output_data) if 'Traceback' not in output_data else {}

        elif method == 'Plaintext':
            output_path = pathlib.Path(f"{output_base_path}/{sentence_hash}.json")
            with open(output_path, 'r') as out_file:
                output = json.loads(out_file.read())

        elif method == 'Code+Execution':
            output_path = pathlib.Path(f"{output_base_path}/{sentence_hash}.txt")
            with open(output_path, 'r') as out_file:
                output = load_text(out_file.read())

        else:
            raise ValueError(f"Unknown method: {method}")

        update_counts(final_states, output, tp_count, fp_count, fn_count, operations_num)

    ac_map = {
        operations_num: tp / (tp + fp + fn)
        for operations_num, tp, fp, fn in
        zip(tp_count.keys(), tp_count.values(), fp_count.values(), fn_count.values())
    }

    return ac_map, tp_count, fp_count, fn_count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process datasets.')
    parser.add_argument('--dataset_path', type=str, required=True, help='Path to the dataset.')
    parser.add_argument('--method', type=str, choices=['Code', 'Plaintext', 'Code+Execution'], required=True,
                        help='Processing method.')
    parser.add_argument('--output_base_path', type=str, required=True, help='Base path for prediction outputs.')

    args = parser.parse_args()

    # Derive the dataset name from the dataset_path
    dataset_filename = pathlib.Path(args.dataset_path).stem  # Get filename without extension
    dataset_name_parts = dataset_filename.split('_')
    dataset_name = ' '.join([part.capitalize() for part in dataset_name_parts])

    accuracy_map, tp, fp, fn = evaluate_dataset(args.dataset_path, args.method, args.output_base_path)

    # Plot and print metrics
    print_metrics(f"{args.method}", dataset_name, tp, fp, fn)
    plotting(accuracy_map, f"{args.method}", dataset_name)

