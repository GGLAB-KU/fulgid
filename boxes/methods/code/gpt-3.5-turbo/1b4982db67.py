# Initialize the boxes
boxes = {
    0: ['coat', 'coffee'],
    1: ['cup', 'fig'],
    2: [],
    3: ['shoe'],
    4: ['crown', 'drug', 'train'],
    5: [],
    6: ['mirror', 'tea'],
}

# Define the moves
moves = [
    (None, 0, 'letter'),    # Put the letter into Box 0
    (0, None, 'letter'),    # Remove the letter from Box 0
    (4, None, 'crown'),     # Remove the crown from Box 4
    (4, None, 'drug'),      # Remove the drug from Box 4
    (4, None, 'train'),     # Remove the train from Box 4
    (None, 6, 'bottle'),    # Put the bottle into Box 6
    (0, None, 'coat'),      # Remove the coat from Box 0
    (6, None, 'bottle'),    # Remove the bottle from Box 6
    (6, None, 'tea'),       # Remove the tea from Box 6
    (6, None, 'mirror'),    # Remove the mirror from Box 6
    (None, 6, 'phone'),     # Put the phone into Box 6
    (None, 6, 'seed'),      # Put the seed into Box 6
    (None, 3, 'jacket'),    # Put the jacket into Box 3
    (6, 4, 'phone'),        # Move the phone from Box 6 to Box 4
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