import argparse
import glob
import json

from boxes.utils import get_sentence_hash_from_path, calculate_metrics
from utils import convert_str_to_dict, execute_code, plotting, load_text

ENGINE = "gpt-3.5-turbo"


def evaluate_dataset(dataset_path, method, output_base_path):
    data_dict = {}

    with open(dataset_path, 'r') as aggregated_boxes_file:
        for json_str in aggregated_boxes_file:
            data = json.loads(json_str)
            sentence_hash = data['sentence_hash']
            data_without_hash = dict(data)
            del data_without_hash['sentence_hash']
            data_dict[sentence_hash] = data_without_hash

    op_f1_score = {}
    box_f1_score = {}

    def calculate_f1_score(counts):
        tp = counts.get('TP', 0)
        fp = counts.get('FP', 0)
        fn = counts.get('FN', 0)
        return 2 * tp / (2 * tp + fp + fn) if (2 * tp + fp + fn) != 0 else 0

    def do_evaluate(box_data, result):
        final_states = box_data.get('final_states')
        box_number = len(final_states) - 1

        # Calculate overall metrics for this sentence
        true_positives, false_positives, false_negatives = calculate_metrics(final_states, result)

        # Box F1 Score
        if box_number not in box_f1_score:
            box_f1_score[box_number] = {'TP': 0, 'FP': 0, 'FN': 0}

        box_f1_score[box_number]['TP'] += true_positives
        box_f1_score[box_number]['FP'] += false_positives
        box_f1_score[box_number]['FN'] += false_negatives

        # Operation-specific metrics
        for op, count in box_data['numops'].items():
            if op not in op_f1_score:
                op_f1_score[op] = {'TP': 0, 'FP': 0, 'FN': 0}

            if count == 0:
                continue

            op_f1_score[op]['TP'] += true_positives / count
            op_f1_score[op]['FP'] += false_positives / count
            op_f1_score[op]['FN'] += false_negatives / count

    def process_output(output_path_list):
        for output_path in output_path_list:
            sentence_hash = get_sentence_hash_from_path(output_path)
            box_data = data_dict.get(sentence_hash)
            if box_data:
                if method == 'Code':
                    output_data = execute_code(output_path)
                    result = convert_str_to_dict(output_data) if 'Traceback' not in output_data else {}
                else:
                    with open(output_path, 'r') as out_file:
                        result = json.loads(out_file.read()) if method == 'Plaintext' else load_text(out_file.read())
                do_evaluate(box_data, result)

    if method == 'Code':
        process_output(glob.glob(f"{output_base_path}/*.py"))
    elif method == 'Plaintext':
        process_output(glob.glob(f"{output_base_path}/*.json"))
    elif method == 'Code+Execution':
        process_output(glob.glob(f"{output_base_path}/*.txt"))

    return {k: calculate_f1_score(v) for k, v in op_f1_score.items()}, {k: calculate_f1_score(v) for k, v in
                                                                        box_f1_score.items()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process datasets.')
    parser.add_argument('--dataset_path', type=str, help='Path to the dataset.',
                        default='datasets/complex_aggregated_data.jsonl')
    parser.add_argument('--method', type=str, choices=['Code', 'Plaintext', 'Code+Execution'],
                        help='Processing method.', default='Plaintext')
    parser.add_argument('--output_base_path', type=str, help='Base path for prediction outputs.',
                        default='results/complex-boxes-dataset/plaintext/gpt-3.5-turbo')

    args = parser.parse_args()

    op_f1_values, box_f1_values = evaluate_dataset(args.dataset_path, args.method, args.output_base_path)

    plotting(op_f1_values, f"{args.method} - Operation-wise F1 Score", "Operation",'Operation', 'F1-score')
    plotting(box_f1_values, f"{args.method} - Box Number-wise F1 Score", "Box Number", 'Number of Boxes', 'F1-score')
