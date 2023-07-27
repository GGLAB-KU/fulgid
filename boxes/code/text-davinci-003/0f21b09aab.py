# Initialize the boxes
boxes = {
    0: ['block', 'disk'],
    1: ['boot', 'brain'],
    2: ['chemical', 'phone', 'seed'],
    3: ['fig', 'mirror', 'pot'],
    4: [],
    5: ['cross', 'sheet', 'shell'],
    6: ['cheese', 'dish', 'painting'],
}

# Define the moves
moves = [
    (3, 4, 'tissue'),       # Put the tissue into Box 4
    (4, None, 'tissue'),    # Remove the tissue from Box 4
    (2, None, 'chemical'),  # Remove the chemical from Box 2
    (2, None, 'phone'),     # Remove the phone from Box 2
    (5, None, 'cross'),     # Remove the cross from Box 5
    (5, None, 'sheet'),     # Remove the sheet from Box 5
    (2, None, 'seed'),      # Remove the seed from Box 2
    (5, 0, 'shell'),        # Move the shell from Box 5 to Box 0
    (0, None, 'disk'),      # Remove the disk from Box 0
    (0, None, 'shell'),     # Remove the shell from Box 0
    (0, 1, 'block'),        # Move the block from Box 0 to Box 1
    (None, 2, 'bowl'),      # Put the bowl into Box 2
    (None, 2, 'ticket'),    # Put the ticket into Box 2
    (None, 4, 'train'),     # Put the train into Box 4
    (None, 5, 'car'),       # Put the car into Box 5
    (None, 5, 'shoe')       # Put the shoe into Box 5
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