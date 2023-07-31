# Initialize the boxes
boxes = {
    0: ['computer'],
    1: [],
    2: [],
    3: ['camera', 'letter', 'picture'],
    4: ['ice', 'machine', 'ticket'],
    5: ['ball', 'cream', 'pot'],
    6: ['file'],
}

# Define the moves
moves = [
    (3, None, 'letter'),        # Remove the letter from Box 3
    (3, None, 'picture'),       # Remove the picture from Box 3
    (None, 3, 'wire'),           # Put the wire into Box 3
    (None, 3, 'sheet'),          # Put the sheet into Box 3
    (3, 1, 'camera'),            # Move the camera from Box 3 to Box 1
    (3, 1, 'sheet'),             # Move the sheet from Box 3 to Box 1
    (3, 1, 'wire'),              # Move the wire from Box 3 to Box 1
    (5, None, 'cream'),          # Remove the cream from Box 5
    (5, None, 'pot'),            # Remove the pot from Box 5
    (None, 6, 'painting'),       # Put the painting into Box 6
    (None, 6, 'radio'),          # Put the radio into Box 6
    (1, None, 'sheet'),          # Remove the sheet from Box 1
    (0, 5, 'computer'),          # Move the computer from Box 0 to Box 5
    (5, 0, 'ball'),              # Move the ball from Box 5 to Box 0
    (None, 1, 'rock')            # Put the rock into Box 1
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