# Initialize the boxes
boxes = {
    0: [],
    1: ['milk', 'pipe'],
    2: [],
    3: [],
    4: [],
    5: ['magazine', 'tie'],
    6: [],
}

# Define the moves
moves = [
    (1, None, 'milk'),       # Remove the milk from Box 1
    (None, 0, 'bag'),        # Put the bag into Box 0
    (None, 0, 'plant'),      # Put the plant into Box 0
    (0, None, 'bag'),        # Remove the bag from Box 0
    (0, None, 'plant'),      # Remove the plant from Box 0
    (None, 1, 'bag'),        # Put the bag into Box 1
    (None, 1, 'clock'),      # Put the clock into Box 1
    (None, 0, 'fig'),        # Put the fig into Box 0
    (None, 3, 'machine'),    # Put the machine into Box 3
    (None, 3, 'cream'),      # Put the cream into Box 3
    (None, 4, 'cigarette'),  # Put the cigarette into Box 4
    (4, None, 'cigarette'),  # Remove the cigarette from Box 4
    (3, None, 'machine'),    # Remove the machine from Box 3
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