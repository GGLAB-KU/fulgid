# Initialize the boxes
boxes = {
    0: ['string', 'tape', 'train'],
    1: ['brain', 'cream'],
    2: ['pot'],
    3: ['shirt'],
    4: ['rose', 'tea'],
    5: ['drug', 'note'],
    6: ['apple', 'shell'],
}

# Define the moves
moves = [
    (4, 6, 'tea'),         # Move the tea from Box 4 to Box 6
    (3, None, 'shirt'),    # Remove the shirt from Box 3
    (None, 2, 'dress'),    # Put the dress into Box 2
    (None, 4, 'picture'),  # Put the picture into Box 4
    (None, 4, 'plant'),    # Put the plant into Box 4
    (1, None, 'cream'),    # Remove the cream from Box 1
    (4, 3, 'picture'),     # Move the picture from Box 4 to Box 3
    (5, None, 'drug'),     # Remove the drug from Box 5
    (4, 5, 'plant'),       # Move the plant from Box 4 to Box 5
    (4, 5, 'rose'),        # Move the rose from Box 4 to Box 5
    (5, 2, 'rose'),        # Move the rose from Box 5 to Box 2
    (3, None, 'picture')   # Remove the picture from Box 3
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