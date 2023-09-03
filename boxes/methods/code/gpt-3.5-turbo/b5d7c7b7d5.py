# Initialize the boxes
boxes = {
    0: ['bag', 'cigarette', 'picture'],
    1: ['boot', 'gift'],
    2: ['clock'],
    3: ['bowl', 'mirror'],
    4: ['dish', 'wire'],
    5: ['coat'],
    6: ['camera', 'creature', 'string'],
}

# Define the moves
moves = [
    (0, 1, 'cigarette'),    # Move the cigarette from Box 0 to Box 1
    (4, None, 'wire'),      # Remove the wire from Box 4
    (1, 5, 'cigarette'),    # Move the cigarette from Box 1 to Box 5
    (1, 5, 'gift'),         # Move the gift from Box 1 to Box 5
    (6, None, 'string'),    # Remove the string from Box 6
    (0, None, 'picture'),   # Remove the picture from Box 0
    (0, 4, 'bag'),          # Move the bag from Box 0 to Box 4
    (6, 0, 'camera'),       # Move the camera from Box 6 to Box 0
    (6, 0, 'creature')      # Move the creature from Box 6 to Box 0
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