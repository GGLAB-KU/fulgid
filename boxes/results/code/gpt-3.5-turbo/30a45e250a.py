# Initialize the boxes
boxes = {
    0: ['computer', 'crown'],
    1: ['beer', 'sheet', 'train'],
    2: ['clock', 'leaf'],
    3: ['picture', 'shoe', 'tie'],
    4: ['glass', 'plate', 'suit'],
    5: [],
    6: ['ticket'],
}

# Define the moves
moves = [
    (3, 6, 'shoe'),         # Move the shoe from Box 3 to Box 6
    (3, 6, 'picture'),      # Move the picture from Box 3 to Box 6
    (1, None, 'sheet'),     # Remove the sheet from Box 1
    (1, None, 'train'),     # Remove the train from Box 1
    (2, None, 'leaf'),      # Remove the leaf from Box 2
    (0, None, 'computer'),  # Remove the computer from Box 0
    (0, None, 'crown'),     # Remove the crown from Box 0
    (None, 3, 'ball'),      # Put the ball into Box 3
    (4, None, 'suit'),      # Remove the suit from Box 4
    (None, 2, 'newspaper'), # Put the newspaper into Box 2
    (None, 0, 'mirror'),    # Put the mirror into Box 0
    (1, None, 'beer'),      # Remove the beer from Box 1
    (None, 3, 'chemical'),  # Put the chemical into Box 3
    (3, None, 'ball'),      # Remove the ball from Box 3
    (3, None, 'chemical'),  # Remove the chemical from Box 3
    (3, None, 'tie')        # Remove the tie from Box 3
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