# Initialize the boxes
boxes = {
    0: ['book', 'fish', 'watch'],
    1: ['branch', 'hat', 'shell'],
    2: ['bread', 'seed'],
    3: ['apple'],
    4: ['brain', 'document'],
    5: ['crown', 'plane'],
    6: ['cup'],
}

# Define the moves
moves = [
    (6, None, 'cup'),       # Remove the cup from Box 6
    (4, None, 'brain'),     # Remove the brain from Box 4
    (4, None, 'document'),  # Remove the document from Box 4
    (2, 4, 'seed'),         # Move the seed from Box 2 to Box 4
    (1, 3, 'branch'),       # Move the branch from Box 1 to Box 3
    (1, 3, 'hat'),          # Move the hat from Box 1 to Box 3
    (2, None, 'bread')      # Remove the bread from Box 2
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