# Initialize the boxes
boxes = {
    0: ['flower', 'magazine'],
    1: ['leaf', 'shell'],
    2: ['apple', 'glass', 'tea'],
    3: ['drug'],
    4: ['bill', 'clock', 'tissue'],
    5: ['knife', 'phone', 'rose'],
    6: ['cigarette', 'sheet', 'shoe'],
}

# Define the moves
moves = [
    (0, None, 'magazine'),   # Remove the magazine from Box 0
    (2, None, 'tea'),        # Remove the tea from Box 2
    (4, None, 'tissue'),     # Remove the tissue from Box 4
    (5, None, 'knife'),      # Remove the knife from Box 5
    (5, None, 'rose'),       # Remove the rose from Box 5
    (6, None, 'cigarette'),  # Remove the cigarette from Box 6
    (6, None, 'sheet'),      # Remove the sheet from Box 6
    (6, None, 'shoe'),       # Remove the shoe from Box 6
    (1, 3, 'shell'),         # Move the shell from Box 1 to Box 3
    (None, 6, 'boat'),       # Put the boat into Box 6
    (3, 5, 'drug'),          # Move the drug from Box 3 to Box 5
    (2, None, 'glass'),      # Remove the glass from Box 2
    (None, 6, 'letter'),     # Put the letter into Box 6
    (None, 6, 'map'),        # Put the map into Box 6
    (0, None, 'flower'),     # Remove the flower from Box 0
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