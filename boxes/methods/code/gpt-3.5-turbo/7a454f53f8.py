# Initialize the boxes
boxes = {
    0: ['coffee', 'egg', 'string'],
    1: ['card', 'pot'],
    2: ['disk'],
    3: ['drug', 'key'],
    4: ['cream'],
    5: ['block', 'creature', 'tea'],
    6: ['rock'],
}

# Define the moves
moves = [
    (None, 1, 'map'),       # Put the map into Box 1
    (1, 4, 'card'),         # Move the card from Box 1 to Box 4
    (1, 4, 'map'),          # Move the map from Box 1 to Box 4
    (2, None, 'disk'),      # Remove the disk from Box 2
    (5, 6, 'block'),        # Move the block from Box 5 to Box 6
    (5, 6, 'creature'),     # Move the creature from Box 5 to Box 6
    (1, None, 'pot'),       # Remove the pot from Box 1
    (3, 2, 'drug'),         # Move the drug from Box 3 to Box 2
    (3, 2, 'key'),          # Move the key from Box 3 to Box 2
    (None, 3, 'boot'),      # Put the boot into Box 3
    (None, 3, 'radio'),     # Put the radio into Box 3
    (3, 5, 'radio'),        # Move the radio from Box 3 to Box 5
    (4, 5, 'map'),          # Move the map from Box 4 to Box 5
    (2, 3, 'key'),          # Move the key from Box 2 to Box 3
    (None, 4, 'plate')      # Put the plate into Box 4
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