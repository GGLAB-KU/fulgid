import hashlib
import os
import random
import json

from settings import Settings

# Extended List of Operations
operations = ["Put", "Move", "Remove", "Empty", "Replace", "Swap"]
content_items = ["the apple", "the book", "the candle", "the pen", "the hat", "the gloves", "the shoes", "the socks",
                 "the watch", "the ring", "the necklace", "the spoon", "the fork", "the shirt", "the pants",
                 "the flashlight", "the mug", "the scarf", "the battery", "the key", "the glasses", "the knife",
                 "the pillow", "the camera", "the tape", "the charger", "the remote", "the map", "the ball",
                 "the painting", "the pliers", "the hammer", "the screwdriver", "the bottle", "the cork", "the wallet",
                 "the perfume", "the brush", "the comb", "the soap", "the toothbrush", "the toothpaste", "the towel",
                 "the umbrella", "the guitar", "the microphone", "the headphones", "the calculator", "the wallet",
                 "the coin", "the phone", "the tablet", "the laptop", "the keyboard", "the mouse", "the blanket",
                 "the lamp", "the clock", "the mirror", "the shovel", "the plant", "the flower", "the scissors",
                 "the plate", "the bowl", "the cup", "the fork", "the knife", "the spoon", "the glass",
                 "the candlestick", "the vase", "the frame", "the portrait", "the fan", "the shampoo",
                 "the conditioner", "the razor", "the hairbrush", "the bandage", "the ointment", "the socks",
                 "the underwear", "the shirt", "the pants", "the dress", "the tie", "the jacket", "the coat",
                 "the belt", "the bracelet", "the watch", "the earrings", "the necklace", "the paper", "the pencil",
                 "the pen", "the marker", "the crayon", "the chalk", "the ruler", "the eraser", "the notebook",
                 "the calendar", "the envelope", "the stamp", "the stapler", "the scissors", "the tape", "the glue",
                 "the folder", "the backpack", "the briefcase", "the lunchbox", "the book", "the magazine",
                 "the newspaper", "the dictionary", "the thesaurus", "the encyclopedia", "the novel", "the poetry",
                 "the biography", "the history", "the fiction", "the nonfiction", "the mystery", "the romance",
                 "the science", "the fantasy", "the adventure", "the horror", "the comedy", "the drama", "the music",
                 "the art", "the film", "the photograph", "the exhibition", "the concert", "the ticket", "the recipe",
                 "the ingredient", "the grocery", "the shopping", "the cart", "the basket", "the bag", "the wallet",
                 "the purse", "the cashier", "the credit", "the debit", "the receipt", "the change", "the coin",
                 "the bank", "the account", "the loan", "the interest", "the investment", "the stock", "the portfolio",
                 "the retirement", "the insurance", "the claim", "the deductible", "the premium", "the coverage",
                 "the policy", "the badge", "the uniform", "the weapon", "the shield"]

file_path_aggregated_data = os.path.join(Settings.boxes_dataset_path, "aggregated_data.jsonl")

sentence_hashes_used = set()  # set to store sentence_hash values


def hash_sentence(text, length=10):
    # To get sentence_hash values
    full_hash = hashlib.sha256(text.encode()).hexdigest()
    return full_hash[:length]


with open(file_path_aggregated_data, "r") as file:
    for line in file:
        data = json.loads(line)  # get the JSON from each line
        sentence_hash = data.get("sentence_hash")  # get the sentence hash of the current JSON
        if sentence_hash:
            sentence_hashes_used.add(sentence_hash)  # add sentence hash to the used hashes set


def generate_procedural_text(total_operations_count, total_boxes_count):
    numops = {"Move": 0, "Remove": 0, "Put": 0, "Empty": 0, "Replace": 0, "Swap": 0, "Total": 0}
    # Randomly generating initial box contents
    box_contents = {}  # Keeping track of box contents for some operations to make sense, e.g. Swap, Replace
    for box_index in range(total_boxes_count):
        num_items = random.randint(0, 4)  # Initially, boxes may contain 0 to 4 items / Which may be changed as needed
        items = []
        for j in range(num_items):
            items.append(random.choice(content_items))
        box_contents[f"Box {box_index}"] = items

    # Now, we have boxes, and their contents

    # Generating box descriptions
    box_descriptions = []
    for box, items in box_contents.items():
        if items:
            description = f"{box} contains {' and '.join(items)}, "
        else:
            description = f"{box} contains nothing, "
        box_descriptions.append(description)

    # Combining box descriptions into a single string
    # E.G. Box 0 contains tape and science and book, Box 1 contains apple, Box 2 contains nothing.
    procedural_text = "".join(box_descriptions)[:-2] + "."

    # Generating operations and keeping track of box contents
    operations_text = []
    for operation_index in range(total_operations_count):
        # Some operations require items in the boxes, which requires to know which boxes contain items
        # E.G. SWAP, MOVE, REPLACE
        boxes_with_items = [box for box, items in box_contents.items() if items]

        operation = random.choice(operations)

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
                box1, box2 = random.sample(boxes_with_items, 2)
                item1 = random.choice(box_contents[box1])
                item2 = random.choice(box_contents[box2])
                while item1 == item2:  # If both are items are the same, search for new ones
                    item1 = random.choice(box_contents[box1])
                    item2 = random.choice(box_contents[box2])

                box_contents[box1].remove(item1)
                box_contents[box2].remove(item2)
                box_contents[box1].append(item2)
                box_contents[box2].append(item1)
                actions = f"{operation} {item1} in {box1} with {item2} in {box2}."

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
    num_operations = random.randint(5, 20)
    num_boxes = random.randint(5, 15)
    example = generate_procedural_text(num_operations, num_boxes)
    example["sample_id"] = sample_id
    data_list.append(example)

# Creating new JSONL file
jsonl_filepath = os.path.join(Settings.boxes_dataset_path, "new_aggregated_data.jsonl")


# Write each JSON object as a line in the JSONL file
with open(jsonl_filepath, 'w') as jsonl_file:
    for data in data_list:
        json_line = json.dumps(data, ensure_ascii=False)
        jsonl_file.write(json_line + '\n')

print(len(sentence_hashes_used))
print("JSONL file created successfully.")
