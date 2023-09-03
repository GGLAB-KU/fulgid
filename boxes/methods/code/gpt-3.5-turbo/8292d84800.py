# Initialize the boxes
boxes = {
    0: ['jacket', 'tape'],
    1: ['ring'],
    2: ['dish'],
    3: ['drink'],
    4: ['ball', 'fan', 'file'],
    5: ['ice', 'radio'],
    6: ['leaf', 'string'],
}

# Define the moves
moves = [
    (2, 3, 'dish'),         # Move the dish from Box 2 to Box 3
    (5, None, 'radio'),     # Remove the radio from Box 5
    (0, None, 'jacket'),    # Remove the jacket from Box 0
    (5, None, 'ice'),       # Remove the ice from Box 5
    (4, 2, 'file'),         # Move the file from Box 4 to Box 2
    (4, None, 'ball'),      # Remove the ball from Box 4
    (4, None, 'fan'),       # Remove the fan from Box 4
    (1, None, 'ring'),      # Remove the ring from Box 1
    (3, 6, 'dish'),         # Move the dish from Box 3 to Box 6
    (2, None, 'file'),      # Remove the file from Box 2
    (3, None, 'drink'),     # Remove the drink from Box 3
    (None, 2, 'knife'),     # Put the knife into Box 2
    (None, 2, 'note'),      # Put the note into Box 2
    (2, None, 'knife'),     # Remove the knife from Box 2
    (2, None, 'note')       # Remove the note from Box 2
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