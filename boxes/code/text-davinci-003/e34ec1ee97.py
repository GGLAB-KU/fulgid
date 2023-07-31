# Initialize the boxes
boxes = {
    0: ['creature', 'magazine'],
    1: ['disk', 'radio'],
    2: ['beer', 'sheet'],
    3: [],
    4: [],
    5: ['ball', 'fig'],
    6: ['bell', 'engine'],
}

# Define the moves
moves = [
    (1, 3, 'disk'),     # Move the disk from Box 1 to Box 3
    (1, 3, 'radio'),    # Move the radio from Box 1 to Box 3
    (None, 4, 'shoe'),  # Put the shoe into Box 4
    (None, 2, 'milk'),  # Put the milk into Box 2
    (6, None, 'bell'),  # Remove the bell from Box 6
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