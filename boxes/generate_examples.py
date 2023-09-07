import pathlib
import random
import json

from preprocess import hash_sentence
from utils import content_items, operations

MAX_EMPTY_ACTIONS = 3

sentence_hashes_used = set()  # set to store sentence_hash values
original_aggregated_path = pathlib.Path("datasets/original_aggregated_data.jsonl")

with open(original_aggregated_path, "r") as file:
    for line in file:
        data = json.loads(line)  # get the JSON from each line
        sentence_hash = data.get("sentence_hash")  # get the sentence hash of the current JSON
        if sentence_hash:
            sentence_hashes_used.add(sentence_hash)  # add sentence hash to the used hashes set


def generate_procedural_text():
    boxes_count = random.randint(5, 15)
    operations_count = int(1.5 * boxes_count)  # 1.5 times the number of boxes

    # Weighted probabilities for each operation
    operation_weights = {
        "Move": 1,
        "Remove": 0.9,
        "Put": 0.9,
        "Empty": 0.2,
        "Replace": 0.8,
        "Swap": 0.8,
    }

    # Preparing operations list before loop
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

    numops = {"Move": 0, "Remove": 0, "Put": 0, "Empty": 0, "Replace": 0, "Swap": 0, "Total": 0}
    shuffled_items = random.sample(content_items, len(content_items))  # This shuffles the entire content_items list

    # Randomly generating initial box contents
    box_contents = {}
    item_index = 0  # This index will keep track of where we are in the shuffled_items list
    for box_index in range(boxes_count):
        num_items = random.randint(0, 5)  # Number of items to be placed in the current box

        # Assign items to the current box, making sure not to exceed the length of shuffled_items
        items_for_box = shuffled_items[item_index: item_index + num_items]

        # Update the item_index for the next iteration
        item_index += num_items

        # Assign the selected items to the current box
        box_contents[f"Box {box_index}"] = items_for_box

    # Now, we have boxes, and their contents
    def describe_box(box_name, items):
        if not items:
            return f"{box_name} contains nothing"
        elif len(items) == 1:
            return f"{box_name} contains the {items[0]}"
        else:
            items_description = ', '.join(f"the {item}" for item in items[:-1]) + ' and ' + f"the {items[-1]}"
            return f"{box_name} contains {items_description}"

    descriptions = [describe_box(box, items) for box, items in box_contents.items()]
    procedural_text = ', '.join(descriptions) + '.'

    # Generating operations and keeping track of box contents
    operations_text = []
    for operation in operations_list:
        # Some operations require items in the boxes, which requires to know which boxes contain items
        # E.G. SWAP, MOVE, REPLACE
        boxes_with_items = [box for box, items in box_contents.items() if items]

        # Keeping track of numops for our JSON
        numops[str(operation)] += 1
        numops["Total"] += 1
        actions = ""
        # THINK OF APPLYING AN OPERATION TO MULTIPLE ITEMS AT THE SAME TIME
        # E.G. Put the dish and the stone into Box 5.
        if operation == "Put":
            destination = random.choice(list(box_contents.keys()))  # First find the destination
            item = random.choice(content_items)
            while item in box_contents[destination]:  # if the item is already there, keep searching for a new item
                item = random.choice(content_items)
            box_contents[destination].append(item)  # Put the item into the box
            actions = f"{operation} {item} into {destination}."

        elif operation == "Move":
            if boxes_with_items:
                source = random.choice(boxes_with_items)

                # Make sure destination is not the same as source
                destination = source
                while destination == source:
                    destination = random.choice(list(box_contents.keys()))

                item = random.choice(box_contents[source])  # Randomly select an item from source box
                box_contents[source].remove(item)
                box_contents[destination].append(item)
                actions = f"{operation} {item} from {source} to {destination}."

        elif operation == "Remove":
            if boxes_with_items:
                box = random.choice(boxes_with_items)
                item = random.choice(box_contents[box])
                box_contents[box].remove(item)
                actions = f"{operation} {item} from {box}."

        elif operation == "Empty":
            if boxes_with_items:
                box = random.choice(boxes_with_items)
                box_contents[box] = []
                actions = f"{operation} {box}."

        elif operation == "Replace":
            if boxes_with_items:
                box = random.choice(boxes_with_items)
                item_to_replace = random.choice(box_contents[box])
                new_item_candidates = [item for item in content_items if item != item_to_replace]
                if new_item_candidates:  # If we have found candidates that is almost always the case
                    new_item = random.choice(new_item_candidates)
                    box_contents[box].remove(item_to_replace)
                    box_contents[box].append(new_item)
                    actions = f"{operation} {item_to_replace} with {new_item} in {box}."

        elif operation == "Swap":
            if len(boxes_with_items) >= 2:  # If there are at least 2 boxes with items, we can do swap
                source, destination = random.sample(boxes_with_items, 2)

                # Randomly select valid indices for source and destination
                source_index = random.randint(0, len(box_contents[source]) - 1)
                destination_index = random.randint(0, len(box_contents[destination]) - 1)

                source_item = box_contents[source][source_index]
                destination_item = box_contents[destination][destination_index]

                # Swap the items at the specified indices
                box_contents[source][source_index] = destination_item
                box_contents[destination][destination_index] = source_item

                actions = f"{operation} {source_item} in {source} with {destination_item} in {destination}."

        operations_text.append(actions)

    # Combining box descriptions and operations: Getting the procedural text
    procedural_text += " " + " ".join(operations_text)

    sentence_hash_value = hash_sentence(procedural_text)
    while sentence_hash_value in sentence_hashes_used:  # check if the current hash has previously been used
        print("PREVIOUSLY USED HASH VALUE")
        sentence_hash_value = hash_sentence(procedural_text)
    sentence_hashes_used.add(sentence_hash_value)

    final_json = {"sentence_hash": sentence_hash_value,
                  "sentence": procedural_text,
                  "sample_id": -1,
                  "numops": numops,
                  "final_states": box_contents}
    return final_json


# # Example usage
data_list = []
for sample_id in range(716):  # 500 examples
    example = generate_procedural_text()
    example["sample_id"] = sample_id
    data_list.append(example)

# Creating new JSONL file
output_path = pathlib.Path("datasets/complex_aggregated_data.jsonl")

# Write each JSON object as a line in the JSONL file
with open(output_path, 'w') as jsonl_file:
    for data in data_list:
        json_line = json.dumps(data, ensure_ascii=False)
        jsonl_file.write(json_line + '\n')

print(len(sentence_hashes_used))
print("JSONL file created successfully.")
