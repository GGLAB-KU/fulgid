# Initialize the boxes
boxes = {
    0: ['cheese', 'guitar', 'string'],
    1: [],
    2: ['brick', 'clock', 'tea'],
    3: ['drug'],
    4: ['apple'],
    5: [],
    6: ['newspaper'],
}

# Define the moves
moves = [
    (None, 3, 'milk'),       # Put the milk into Box 3
    (2, None, 'tea'),        # Remove the tea from Box 2
    (0, 1, 'string'),        # Move the string from Box 0 to Box 1
    (4, 1, 'apple'),         # Move the apple from Box 4 to Box 1
    (2, None, 'brick'),      # Remove the brick from Box 2
    (2, None, 'clock'),      # Remove the clock from Box 2
    (1, None, 'string'),     # Remove the string from Box 1
    (1, None, 'apple'),      # Remove the apple from Box 1
    (3, None, 'drug'),       # Remove the drug from Box 3
    (None, 6, 'camera'),     # Put the camera into Box 6
    (None, 6, 'fig'),        # Put the fig into Box 6
    (6, 1, 'camera')         # Move the camera from Box 6 to Box 1
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