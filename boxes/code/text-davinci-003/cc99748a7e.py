# Initialize the boxes
boxes = {
    0: ['key'],
    1: ['dish', 'mirror'],
    2: ['milk'],
    3: ['drug', 'plane', 'shirt'],
    4: ['computer', 'ice'],
    5: ['magazine', 'seed'],
    6: ['block', 'picture'],
}

# Define the moves
moves = [
    (None, 2, 'drink'),        # Put the drink into Box 2
    (4, 1, 'computer'),         # Move the computer from Box 4 to Box 1
    (4, None, 'ice'),           # Remove the ice from Box 4
    (3, 2, 'drug'),             # Move the drug from Box 3 to Box 2
    (3, 5, 'shirt'),            # Move the shirt from Box 3 to Box 5
    (3, None, 'plane'),         # Remove the plane from Box 3
    (0, 6, 'key'),              # Move the key from Box 0 to Box 6
    (6, None, 'block'),         # Remove the block from Box 6
    (5, 3, 'magazine'),         # Move the magazine from Box 5 to Box 3
    (5, 3, 'seed'),             # Move the seed from Box 5 to Box 3
    (2, None, 'drink'),         # Remove the drink from Box 2
    (2, None, 'milk'),          # Remove the milk from Box 2
    (1, None, 'computer')       # Remove the computer from Box 1
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