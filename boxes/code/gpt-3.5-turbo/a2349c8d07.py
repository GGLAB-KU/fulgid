# Initialize the boxes
boxes = {
    0: ['block', 'rock'],
    1: ['apple'],
    2: ['coat', 'flower'],
    3: ['bill', 'camera', 'disk'],
    4: ['bag', 'key', 'letter'],
    5: ['shoe'],
    6: [],
}

# Define the moves
moves = [
    (5, None, 'shoe'),       # Remove the shoe from Box 5
    (2, 6, 'coat'),          # Move the coat from Box 2 to Box 6
    (None, 5, 'mirror'),     # Put the mirror into Box 5
    (1, 2, 'apple'),         # Move the apple from Box 1 to Box 2
    (4, 5, 'key'),           # Move the key from Box 4 to Box 5
    (4, 5, 'letter'),        # Move the letter from Box 4 to Box 5
    (4, 1, 'bag'),           # Move the bag from Box 4 to Box 1
    (2, 0, 'flower'),        # Move the flower from Box 2 to Box 0
    (3, 1, 'camera'),        # Move the camera from Box 3 to Box 1
    (None, 6, 'radio'),      # Put the radio into Box 6
    (5, 3, 'letter')         # Move the letter from Box 5 to Box 3
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