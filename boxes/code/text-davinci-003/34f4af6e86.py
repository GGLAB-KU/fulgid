# Initialize the boxes
boxes = {
    0: ['bomb', 'drug'],
    1: ['bill', 'cup', 'plant'],
    2: ['branch', 'card', 'pot'],
    3: ['coffee', 'shell', 'train'],
    4: ['picture', 'rose'],
    5: ['egg'],
    6: ['cash', 'key', 'phone'],
}

# Define the moves
moves = [
    (4, None, 'picture'),   # Remove the picture from Box 4
    (4, None, 'rose'),      # Remove the rose from Box 4
    (5, None, 'egg'),       # Remove the egg from Box 5
    (0, 4, 'drug'),         # Move the drug from Box 0 to Box 4
    (3, 5, 'coffee'),       # Move the coffee from Box 3 to Box 5
    (4, 3, 'drug'),         # Move the drug from Box 4 to Box 3
    (2, None, 'card'),      # Remove the card from Box 2
    (3, None, 'shell'),     # Remove the shell from Box 3
    (3, None, 'train'),     # Remove the train from Box 3
    (None, 2, 'card'),      # Put the card into Box 2
    (5, None, 'coffee')     # Remove the coffee from Box 5
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