# Initialize the boxes
boxes = {
    0: ['cake', 'crown', 'knife'],
    1: ['note'],
    2: ['coat', 'medicine', 'shirt'],
    3: ['bag', 'magazine', 'tissue'],
    4: ['ice'],
    5: ['gift', 'painting', 'shell'],
    6: [],
}

# Define the moves
moves = [
    (5, 1, 'shell'),        # Move the shell from Box 5 to Box 1
    (4, None, 'ice'),       # Remove the ice from Box 4
    (2, 1, 'shirt'),        # Move the shirt from Box 2 to Box 1
    (None, 4, 'card'),      # Put the card into Box 4
    (3, 4, 'magazine'),     # Move the magazine from Box 3 to Box 4
    (3, 4, 'tissue'),       # Move the tissue from Box 3 to Box 4
    (4, None, 'tissue'),    # Remove the tissue from Box 4
    (2, 4, 'medicine'),     # Move the medicine from Box 2 to Box 4
    (None, 2, 'pot'),       # Put the pot into Box 2
    (None, 2, 'tissue'),    # Put the tissue into Box 2
    (1, 6, 'note'),         # Move the note from Box 1 to Box 6
    (4, None, 'card'),      # Remove the card from Box 4
    (4, None, 'magazine'),  # Remove the magazine from Box 4
    (4, None, 'medicine')   # Remove the medicine from Box 4
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