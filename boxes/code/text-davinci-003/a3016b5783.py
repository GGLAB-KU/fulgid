# Initialize the boxes
boxes = {
    0: ['bread', 'bus', 'shoe'],
    1: ['bag'],
    2: ['bottle', 'pot', 'seed'],
    3: ['camera', 'machine', 'wire'],
    4: ['cup', 'glass'],
    5: ['radio', 'tea'],
    6: ['clock', 'medicine', 'paper'],
}

# Define the moves
moves = [
    (6, None, 'paper'),       # Remove the paper from Box 6
    (3, None, 'machine'),     # Remove the machine from Box 3
    (3, None, 'wire'),        # Remove the wire from Box 3
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