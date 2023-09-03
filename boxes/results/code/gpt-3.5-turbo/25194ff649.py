# Initialize the boxes
boxes = {
    0: ['bone'],
    1: ['block'],
    2: ['brain', 'cigarette'],
    3: ['cross', 'drug'],
    4: [],
    5: [],
    6: ['beer', 'coffee'],
}

# Define the moves
moves = [
    (3, 0, 'drug'),         # Move the drug from Box 3 to Box 0
    (None, 3, 'cup'),       # Put the cup into Box 3
    (None, 3, 'picture'),   # Put the picture into Box 3
    (2, 6, 'brain'),        # Move the brain from Box 2 to Box 6
    (3, None, 'cup'),       # Remove the cup from Box 3
    (3, None, 'picture'),   # Remove the picture from Box 3
    (1, 5, 'block'),        # Move the block from Box 1 to Box 5
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