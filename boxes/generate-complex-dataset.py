import pathlib
import random
import json
from preprocess import hash_sentence
from utils import content_items, operations

MAX_EMPTY_ACTIONS = 3


def generate_box_contents(boxes_count):
    shuffled_items = random.sample(content_items, len(content_items))
    box_contents = {}
    item_index = 0
    for box_index in range(boxes_count):
        num_items = random.randint(0, 5)
        items_for_box = shuffled_items[item_index: item_index + num_items]
        item_index += num_items
        box_contents[f"Box {box_index}"] = items_for_box
    return box_contents


def describe_box(box_name, items):
    if not items:
        return f"{box_name} contains nothing"
    elif len(items) == 1:
        return f"{box_name} contains the {items[0]}"
    else:
        items_description = ' and '.join(f"the {item}" for item in items)
        return f"{box_name} contains {items_description}"


def describe_items(items):
    if len(items) == 1:
        return f"the {items[0]}"
    else:
        items_description = ' and '.join(f"the {item}" for item in items)
        return items_description


def describe_final_state(items):
    if not items:
        return ["nothing"]
    else:
        return [f"the {item}" for item in items]


def put_operation(box_contents):
    destination = random.choice(list(box_contents.keys()))
    num_items_to_put = random.randint(1, 3)
    items = [random.choice(content_items) for _ in range(num_items_to_put)]
    # Ensure there are no duplicates
    items = list(set(items))
    for item in items:
        while item in box_contents[destination]:
            item = random.choice(content_items)
        box_contents[destination].append(item)
    return f"Put {describe_items(items)} into {destination}.", box_contents


def move_operation(box_contents, boxes_with_items):
    source = random.choice(boxes_with_items)
    destination = source
    while destination == source:
        destination = random.choice(list(box_contents.keys()))
    num_items_to_move = random.randint(1, min(3, len(box_contents[source])))
    items = random.sample(box_contents[source], num_items_to_move)
    for item in items:
        box_contents[source].remove(item)
        box_contents[destination].append(item)
    return f"Move {describe_items(items)} from {source} to {destination}.", box_contents


def remove_operation(box_contents, boxes_with_items):
    box = random.choice(boxes_with_items)
    num_items_to_remove = random.randint(1, min(3, len(box_contents[box])))
    items = random.sample(box_contents[box], num_items_to_remove)
    for item in items:
        box_contents[box].remove(item)
    return f"Remove {describe_items(items)} from {box}.", box_contents


def empty_operation(box_contents, boxes_with_items):
    box = random.choice(boxes_with_items)
    box_contents[box] = []
    return f"Empty {box}.", box_contents


def replace_operation(box_contents, boxes_with_items):
    box = random.choice(boxes_with_items)
    num_items_to_replace = random.randint(1, min(3, len(box_contents[box])))
    items_to_replace = random.sample(box_contents[box], num_items_to_replace)
    new_items_candidates = [item for item in content_items if item not in items_to_replace]
    new_items = random.sample(new_items_candidates, num_items_to_replace)
    for idx, item_to_replace in enumerate(items_to_replace):
        box_contents[box].remove(item_to_replace)
        box_contents[box].append(new_items[idx])
    return (f"Replace {describe_items(items_to_replace)} with "
            f"{describe_items(new_items)} in {box}."), box_contents


def swap_operation(box_contents, boxes_with_items):
    source, destination = random.sample(boxes_with_items, 2)
    source_index = random.randint(0, len(box_contents[source]) - 1)
    destination_index = random.randint(0, len(box_contents[destination]) - 1)
    source_item = box_contents[source][source_index]
    destination_item = box_contents[destination][destination_index]
    box_contents[source][source_index] = destination_item
    box_contents[destination][destination_index] = source_item
    return (f"Swap the {source_item} in {source} with the {destination_item} "
            f"in {destination}."), box_contents


def apply_operation(operation, box_contents):
    boxes_with_items = [box for box, items in box_contents.items() if items]

    if operation == "Put":
        return put_operation(box_contents)
    elif operation == "Move" and boxes_with_items:
        return move_operation(box_contents, boxes_with_items)
    elif operation == "Remove" and boxes_with_items:
        return remove_operation(box_contents, boxes_with_items)
    elif operation == "Empty" and boxes_with_items:
        return empty_operation(box_contents, boxes_with_items)
    elif operation == "Replace" and boxes_with_items:
        return replace_operation(box_contents, boxes_with_items)
    elif operation == "Swap" and len(boxes_with_items) >= 2:
        return swap_operation(box_contents, boxes_with_items)
    else:
        return "", box_contents


def generate_procedural_text(sentence_hashes_used):
    boxes_count = random.randint(5, 15)
    operations_count = int(1.5 * boxes_count)
    operation_weights = {
        "Move": 1, "Remove": 0.9, "Put": 0.9, "Empty": 0.2, "Replace": 0.8, "Swap": 0.8
    }
    operations_list = random.choices(
        operations,
        weights=[operation_weights[op] for op in operations],
        k=operations_count
    )

    # Limiting Empty action to MAX_EMPTY_ACTIONS
    empty_counter = operations_list.count("Empty")
    while empty_counter > MAX_EMPTY_ACTIONS:
        operations_list.remove("Empty")
        operations_list.append(random.choice([op for op in operations if op != "Empty"]))
        empty_counter = operations_list.count("Empty")

    box_contents = generate_box_contents(boxes_count)
    descriptions = [describe_box(box, items) for box, items in box_contents.items()]
    procedural_text = ', '.join(descriptions) + '.'

    operations_text = []
    for operation in operations_list:
        action, box_contents = apply_operation(operation, box_contents)
        operations_text.append(action)

    procedural_text += " " + " ".join(operations_text)
    sentence_hash_value = hash_sentence(procedural_text)
    while sentence_hash_value in sentence_hashes_used:
        print("PREVIOUSLY USED HASH VALUE")
        sentence_hash_value = hash_sentence(procedural_text)

    sentence_hashes_used.add(sentence_hash_value)

    numops = {op: operations_list.count(op) for op in operations}
    numops["Total"] = len(operations_list)

    final_states = {box: describe_final_state(items) for box, items in box_contents.items()}
    final_json = {
        "sentence_hash": sentence_hash_value, "sentence": procedural_text,
        "sample_id": -1, "numops": numops, "final_states": final_states
    }

    return final_json, sentence_hashes_used


def main():
    original_aggregated_path = pathlib.Path("datasets/original_aggregated_data.jsonl")
    sentence_hashes_used = set()

    with open(original_aggregated_path, "r") as file:
        for line in file:
            data = json.loads(line)
            sentence_hash = data.get("sentence_hash")
            if sentence_hash:
                sentence_hashes_used.add(sentence_hash)

    data_list = []
    for sample_id in range(716):
        example, sentence_hashes_used = generate_procedural_text(sentence_hashes_used)
        example["sample_id"] = sample_id
        data_list.append(example)

    output_path = pathlib.Path("datasets/complex_aggregated_data.jsonl")

    with open(output_path, 'w') as jsonl_file:
        for data in data_list:
            json_line = json.dumps(data, ensure_ascii=False)
            jsonl_file.write(json_line + '\n')

    print(len(sentence_hashes_used))
    print("JSONL file created successfully.")


if __name__ == "__main__":
    main()
