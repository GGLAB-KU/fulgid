# Initialize the boxes
boxes = {
    0: [],
    1: [],
    2: ['meat'],
    3: ['fan'],
    4: ['bell'],
    5: ['map'],
    6: ['bottle', 'car', 'document'],
}

# Define the moves
moves = [
    (2, None, 'meat'),       # Remove the meat from Box 2
    (5, 0, 'map'),           # Move the map from Box 5 to Box 0
    (6, None, 'bottle'),     # Remove the bottle from Box 6
    (6, None, 'car'),        # Remove the car from Box 6
    (1, None, 'clock'),      # Put the clock into Box 1
    (1, None, 'glass'),      # Put the glass into Box 1
    (6, None, 'document'),   # Remove the document from Box 6
    (1, 0, 'glass'),         # Move the glass from Box 1 to Box 0
    (None, 2, 'cigarette'),  # Put the cigarette into Box 2
    (None, 2, 'creature'),   # Put the creature into Box 2
    (0, 1, 'glass'),         # Move the glass from Box 0 to Box 1
    (0, 1, 'map'),           # Move the map from Box 0 to Box 1
    (3, None, 'fan'),        # Remove the fan from Box 3
    (1, None, 'map'),        # Remove the map from Box 1
    (2, 1, 'creature'),      # Move the creature from Box 2 to Box 1
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