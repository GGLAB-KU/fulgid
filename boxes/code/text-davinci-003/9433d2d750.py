# Initialize the boxes
boxes = {
    0: ['seed', 'train'],
    1: ['ball', 'flower', 'shell'],
    2: ['bottle', 'plant', 'radio'],
    3: [],
    4: ['bag', 'jacket'],
    5: ['map', 'picture'],
    6: [],
}

# Define the moves
moves = [
    (2, None, 'bottle'),    # Remove the bottle from Box 2
    (None, 4, 'fig'),       # Put the fig into Box 4
    (None, 2, 'computer'),  # Put the computer into Box 2
    (2, None, 'computer'),  # Remove the computer from Box 2
    (2, None, 'plant'),     # Remove the plant from Box 2
    (2, None, 'radio'),     # Remove the radio from Box 2
    (None, 6, 'note'),      # Put the note into Box 6
    (6, 3, 'note'),         # Move the note from Box 6 to Box 3
    (4, 6, 'fig'),          # Move the fig from Box 4 to Box 6
    (4, 6, 'jacket')        # Move the jacket from Box 4 to Box 6
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