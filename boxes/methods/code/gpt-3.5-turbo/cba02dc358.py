# Initialize the boxes
boxes = {
    0: ['block', 'bottle', 'wire'],
    1: ['boot', 'cheese', 'leaf'],
    2: ['meat'],
    3: ['bomb', 'game'],
    4: ['bone', 'jacket', 'letter'],
    5: ['plane'],
    6: ['bell', 'cash', 'ice'],
}

# Define the moves
moves = [
    (1, None, 'cheese'),    # Remove the cheese from Box 1
    (2, None, 'meat'),      # Remove the meat from Box 2
    (None, 5, 'cup'),       # Put the cup into Box 5
    (None, 5, 'shell'),     # Put the shell into Box 5
    (6, None, 'bell'),      # Remove the bell from Box 6
    (3, 2, 'bomb'),         # Move the bomb from Box 3 to Box 2
    (4, None, 'jacket'),    # Remove the jacket from Box 4
    (4, None, 'letter')     # Remove the letter from Box 4
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