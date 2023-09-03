# Initialize the boxes
boxes = {
    0: ['brain', 'cigarette'],
    1: ['cheese', 'chemical'],
    2: ['bowl', 'tie'],
    3: ['guitar'],
    4: ['camera'],
    5: ['creature', 'ice'],
    6: ['bomb', 'shirt', 'shoe'],
}

# Define the moves
moves = [
    (5, None, 'ice'),       # Remove the ice from Box 5
    (6, 3, 'shirt'),        # Move the shirt from Box 6 to Box 3
    (2, None, 'bowl'),      # Remove the bowl from Box 2
    (0, 6, 'cigarette'),    # Move the cigarette from Box 0 to Box 6
    (5, None, 'creature'),  # Remove the creature from Box 5
    (3, None, 'shirt'),     # Remove the shirt from Box 3
    (3, None, 'guitar'),    # Remove the guitar from Box 3
    (4, 1, 'camera'),       # Move the camera from Box 4 to Box 1
    (0, 2, 'brain'),        # Move the brain from Box 0 to Box 2
    (None, 3, 'card'),      # Put the card into Box 3
    (None, 3, 'paper'),     # Put the paper into Box 3
    (None, 3, 'plant'),     # Put the plant into Box 3
    (None, 0, 'train')      # Put the train into Box 0
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