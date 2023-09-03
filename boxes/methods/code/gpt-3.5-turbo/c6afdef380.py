# Initialize the boxes
boxes = {
    0: [],
    1: ['coat', 'creature'],
    2: ['cross', 'jacket', 'knife'],
    3: ['pot', 'ring'],
    4: ['ball', 'glass', 'phone'],
    5: ['drink', 'hat', 'picture'],
    6: ['tie'],
}

# Define the moves
moves = [
    (None, 0, 'guitar'),        # Put the guitar into Box 0
    (1, 0, 'coat'),             # Move the coat from Box 1 to Box 0
    (1, 0, 'creature'),         # Move the creature from Box 1 to Box 0
    (6, None, 'tie'),           # Remove the tie from Box 6
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