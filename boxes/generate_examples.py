import random

# Extended List of Operations
operations = ["Put", "Move", "Remove", "Empty", "Replace", "Swap"]
content_items = ["apple", "book", "candle", "pen", "hat", "gloves", "shoes", "socks", "watch", "ring",
                 "necklace", "spoon", "fork", "shirt", "pants", "flashlight", "mug", "scarf", "battery",
                 "key", "glasses", "knife", "pillow", "camera", "tape", "charger", "remote",
                 "map", "ball", "painting", "pliers", "hammer", "screwdriver", "bottle", "cork",
                 "wallet", "perfume", "brush", "comb", "soap", "toothbrush", "toothpaste", "towel",
                 "umbrella", "guitar", "microphone", "headphones", "calculator", "wallet", "coin", "phone",
                 "tablet", "laptop", "keyboard", "mouse", "blanket", "lamp", "clock", "mirror",
                 "shovel", "plant", "flower", "scissors", "plate", "bowl", "cup", "fork", "knife",
                 "spoon", "glass", "candlestick", "vase", "frame", "portrait", "fan", "shampoo",
                 "conditioner", "razor", "hairbrush", "bandage", "ointment", "socks", "underwear", "shirt",
                 "pants", "dress", "tie", "jacket", "coat", "belt", "bracelet", "watch", "earrings",
                 "necklace", "paper", "pencil", "pen", "marker", "crayon", "chalk", "ruler", "eraser",
                 "notebook", "calendar", "envelope", "stamp", "stapler", "scissors", "tape", "glue",
                 "folder", "backpack", "briefcase", "lunchbox", "book", "magazine", "newspaper", "dictionary",
                 "thesaurus", "encyclopedia", "novel", "poetry", "biography", "history", "fiction", "nonfiction",
                 "mystery", "romance", "science", "fantasy", "adventure", "horror", "comedy", "drama",
                 "music", "art", "film", "photograph", "exhibition", "concert", "ticket",
                 "recipe", "ingredient", "grocery", "shopping", "cart", "basket", "bag", "wallet", "purse",
                 "cashier", "credit", "debit", "receipt", "change", "coin", "bank",
                 "account", "loan", "interest", "investment", "stock", "portfolio", "retirement", "insurance",
                 "claim", "deductible", "premium", "coverage", "policy", "badge", "uniform", "weapon", "shield"]


def generate_procedural_text(total_operations_count, total_boxes_count):
    # Randomly generating initial box contents
    box_contents = {}  # Keeping track of box contents for some operations to make sense, e.g. Swap, Replace
    for i in range(total_boxes_count):
        num_items = random.randint(0, 4)  # Initially, boxes may contain 0 to 4 items / Which may be changed as needed
        items = []
        for j in range(num_items):
            items.append(random.choice(content_items))
        box_contents[f"Box {i}"] = items
    # print(box_contents)

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
    # print(procedural_text)

    # Generating operations and keeping track of box contents
    operations_text = []
    for i in range(total_operations_count):
        # Some operations require items in the boxes, which requires to know which boxes contain items
        # E.G. SWAP, MOVE, REPLACE
        boxes_with_items = [box for box, items in box_contents.items() if items]

        operation = random.choice(operations)
        # THINK OF APPLYING AN OPERATION TO MULTIPLE ITEMS AT THE SAME TIME
        # E.G. Put the dish and the stone into Box 5.
        if operation == "Put":
            destination = random.choice(list(box_contents.keys()))  # First find the destination
            item = random.choice(content_items)
            while item in box_contents[destination]:    # if the item is already there, keep searching for a new item
                item = random.choice(content_items)
            box_contents[destination].append(item)  # Put the item into the box
            actions = f"{operation} the {item} into {destination}."

        elif operation == "Move":
            if boxes_with_items:
                source = random.choice(boxes_with_items)
                destination = random.choice(list(box_contents.keys()))
                item = random.choice(box_contents[source])  # Randomly select an item from source box
                # print(box_contents[destination])
                # print(item)
                box_contents[source].remove(item)
                box_contents[destination].append(item)
                actions = f"{operation} the {item} from {source} to {destination}."

        elif operation == "Remove":
            if boxes_with_items:
                box = random.choice(boxes_with_items)
                item = random.choice(box_contents[box])
                box_contents[box].remove(item)
                actions = f"{operation} the {item} from {box}."

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
                    actions = f"{operation} the {item_to_replace} with the {new_item} in {box}."

        elif operation == "Swap":
            if len(boxes_with_items) >= 2:  # If there are at least 2 boxes with items, we can do swap
                box1, box2 = random.sample(boxes_with_items, 2)
                item1 = random.choice(box_contents[box1])
                item2 = random.choice(box_contents[box2])
                while item1 == item2:   # If both are items are the same, search for new ones
                    item1 = random.choice(box_contents[box1])
                    item2 = random.choice(box_contents[box2])

                box_contents[box1].remove(item1)
                box_contents[box2].remove(item2)
                box_contents[box1].append(item2)
                box_contents[box2].append(item1)
                actions = f"{operation} the {item1} in {box1} with the {item2} in {box2}."

        operations_text.append(actions)

    # Combining box descriptions and operations: Getting the procedural text
    procedural_text += " " + " ".join(operations_text)
    # print(procedural_text)
    return procedural_text, box_contents


# # Example usage
num_operations = int(input("Enter the number of total operations: "))
num_boxes = int(input("Enter the number of boxes: "))

procedural_text, final_states = generate_procedural_text(num_operations, num_boxes)
print(procedural_text)
print(final_states)

