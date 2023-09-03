# Initialize the boxes
boxes = {
    0: [],
    1: ['plant', 'seed'],
    2: [],
    3: ['crown', 'newspaper', 'television'],
    4: [],
    5: ['bag', 'hat', 'picture'],
    6: ['bottle', 'document', 'pot'],
}

# Define the moves
moves = [
    (None, 2, 'branch'),    # Put the branch into Box 2
    (1, None, 'plant'),     # Remove the plant from Box 1
    (1, None, 'seed'),      # Remove the seed from Box 1
    (6, None, 'bottle')     # Remove the bottle from Box 6
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