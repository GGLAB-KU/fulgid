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
    (None, 0, 'guitar'),       # Put the guitar into Box 0
    (1, 0, 'coat'),            # Move the coat from Box 1 to Box 0
    (1, 0, 'creature'),        # Move the creature from Box 1 to Box 0
    (6, None, 'tie'),          # Remove the tie from Box 6
    (4, None, 'ball'),         # Remove the ball from Box 4
    (4, None, 'glass'),        # Remove the glass from Box 4
    (None, 6, 'newspaper'),    # Put the newspaper into Box 6
    (None, 6, 'plane'),        # Put the plane into Box 6
    (2, None, 'cross'),        # Remove the cross from Box 2
    (2, None, 'knife'),        # Remove the knife from Box 2
    (0, None, 'creature'),     # Remove the creature from Box 0
    (3, 2, 'pot'),             # Move the pot from Box 3 to Box 2
    (3, 2, 'ring'),            # Move the ring from Box 3 to Box 2
    (2, 3, 'pot'),             # Move the pot from Box 2 to Box 3
    (2, 3, 'ring'),            # Move the ring from Box 2 to Box 3
    (None, 1, 'bone'),         # Put the bone into Box 1
    (None, 1, 'car'),          # Put the car into Box 1
    (None, 1, 'drug')          # Put the drug into Box 1
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