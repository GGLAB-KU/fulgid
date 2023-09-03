# Initialize the boxes
boxes = {
    0: [],
    1: ['cash', 'meat', 'painting'],
    2: ['car'],
    3: [],
    4: ['bowl', 'clock', 'seed'],
    5: [],
    6: ['engine', 'guitar', 'leaf'],
}

# Define the moves
moves = [
    (None, 3, 'coat'),       # Put the coat into Box 3
    (None, 3, 'newspaper'),  # Put the newspaper into Box 3
    (1, None, 'painting'),   # Remove the painting from Box 1
    (4, None, 'bowl'),       # Remove the bowl from Box 4
    (4, None, 'seed'),       # Remove the seed from Box 4
    (None, 0, 'glass'),      # Put the glass into Box 0
    (0, None, 'glass'),      # Remove the glass from Box 0
    (4, 5, 'clock'),         # Move the clock from Box 4 to Box 5
    (None, 4, 'train'),      # Put the train into Box 4
    (4, None, 'train'),      # Remove the train from Box 4
    (6, None, 'guitar'),     # Remove the guitar from Box 6
    (None, 1, 'shoe'),       # Put the shoe into Box 1
    (2, None, 'car'),        # Remove the car from Box 2
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