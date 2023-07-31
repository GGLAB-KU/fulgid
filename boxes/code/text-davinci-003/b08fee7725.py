# Initialize the boxes
boxes = {
    0: [],
    1: ['bone', 'glass'],
    2: ['drink', 'mirror'],
    3: ['apple', 'tie', 'wheel'],
    4: ['ball', 'letter', 'string'],
    5: ['creature', 'guitar', 'sheet'],
    6: ['seed'],
}

# Define the moves
moves = [
    (2, 1, 'mirror'),       # Move the mirror from Box 2 to Box 1
    (6, None, 'seed'),      # Remove the seed from Box 6
    (3, 6, 'wheel'),        # Move the wheel from Box 3 to Box 6
    (None, 2, 'bag'),       # Put the bag into Box 2
    (None, 2, 'branch'),    # Put the branch into Box 2
    (2, 0, 'branch'),       # Move the branch from Box 2 to Box 0
    (2, 0, 'drink'),        # Move the drink from Box 2 to Box 0
    (3, None, 'tie'),       # Remove the tie from Box 3
    (3, None, 'apple'),     # Remove the apple from Box 3
    (0, None, 'branch'),    # Remove the branch from Box 0
    (0, None, 'drink')      # Remove the drink from Box 0
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