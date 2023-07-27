# Initialize the boxes
boxes = {
    0: ['car'],
    1: ['sheet'],
    2: ['chemical', 'mirror'],
    3: ['clock', 'creature', 'picture'],
    4: ['ice'],
    5: [],
    6: ['dish'],
}

# Define the moves
moves = [
    (None, 6, 'milk'),       # Put the milk into Box 6
    (None, 6, 'shell'),      # Put the shell into Box 6
    (6, 4, 'dish'),          # Move the dish from Box 6 to Box 4
    (3, None, 'clock'),      # Remove the clock from Box 3
    (3, None, 'picture'),    # Remove the picture from Box 3
    (None, 3, 'wheel'),      # Put the wheel into Box 3
    (3, 6, 'wheel'),         # Move the wheel from Box 3 to Box 6
    (0, 3, 'car'),           # Move the car from Box 0 to Box 3
    (None, 1, 'camera'),     # Put the camera into Box 1
    (None, 1, 'map'),        # Put the map into Box 1
    (6, None, 'shell'),      # Remove the shell from Box 6
    (6, None, 'milk'),       # Remove the milk from Box 6
    (6, 0, 'wheel'),         # Move the wheel from Box 6 to Box 0
    (1, 5, 'camera'),        # Move the camera from Box 1 to Box 5
    (1, 5, 'map'),           # Move the map from Box 1 to Box 5
    (3, None, 'car'),        # Remove the car from Box 3
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