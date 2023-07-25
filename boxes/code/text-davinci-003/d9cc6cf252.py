# Initialize the boxes
boxes = {
    0: [],
    1: [],
    2: ['radio', 'tissue'],
    3: ['bell', 'chemical'],
    4: ['creature', 'flower', 'shoe'],
    5: ['drug'],
    6: ['computer', 'dish', 'tie'],
}

# Define the moves
moves = [
    (4, 1, 'creature'),     # Move the creature from Box 4 to Box 1
    (4, 1, 'flower'),       # Move the flower from Box 4 to Box 1
    (4, 1, 'shoe'),         # Move the shoe from Box 4 to Box 1
    (3, None, 'bell'),      # Remove the bell from Box 3
    (3, None, 'chemical'),  # Remove the chemical from Box 3
    (2, 5, 'tissue'),       # Move the tissue from Box 2 to Box 5
    (2, None, 'radio'),     # Remove the radio from Box 2
    (None, 2, 'bottle'),    # Put the bottle into Box 2
    (None, 4, 'string'),    # Put the string into Box 4
    (2, 4, 'bottle'),       # Move the bottle from Box 2 to Box 4
    (1, None, 'creature'),  # Remove the creature from Box 1
    (1, None, 'flower'),    # Remove the flower from Box 1
    (1, None, 'shoe'),      # Remove the shoe from Box 1
    (4, 3, 'bottle'),       # Move the bottle from Box 4 to Box 3
    (None, 2, 'bag'),       # Put the bag into Box 2
    (None, 2, 'bus'),       # Put the bus into Box 2
    (None, 2, 'cup'),       # Put the cup into Box 2
    (6, 1, 'dish'),         # Move the dish from Box 6 to Box 1
]

# Execute the moves
for move in moves:
    src, dest, item = move

    if src is not None:  # If there's a source box, remove item from it
        boxes[src].remove(item)

    if dest is not None:  # If there's a destination box, add item to it
        boxes[dest].append(item)

# Print the boxes
for box in boxes:
    print(f"Box {box}: {boxes[box]}")