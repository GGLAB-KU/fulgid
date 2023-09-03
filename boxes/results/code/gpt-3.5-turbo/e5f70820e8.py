# Initialize the boxes
boxes = {
    0: ['boot'],
    1: ['clock', 'guitar'],
    2: ['jacket'],
    3: ['dress', 'fig'],
    4: ['file', 'pot', 'tie'],
    5: ['bowl', 'computer', 'drug'],
    6: ['knife'],
}

# Define the moves
moves = [
    (2, None, 'jacket'),    # Remove the jacket from Box 2
    (4, None, 'file'),      # Remove the file from Box 4
    (4, None, 'tie'),       # Remove the tie from Box 4
    (None, 2, 'coat'),      # Put the coat into Box 2
    (None, 2, 'letter'),    # Put the letter into Box 2
    (None, 2, 'ring'),      # Put the ring into Box 2
    (2, None, 'coat'),      # Remove the coat from Box 2
    (2, None, 'letter'),    # Remove the letter from Box 2
    (2, None, 'ring'),      # Remove the ring from Box 2
    (5, None, 'bowl'),      # Remove the bowl from Box 5
    (3, None, 'dress'),     # Remove the dress from Box 3
    (3, None, 'fig'),       # Remove the fig from Box 3
    (0, 5, 'boot'),         # Move the boot from Box 0 to Box 5
    (6, None, 'knife'),     # Remove the knife from Box 6
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