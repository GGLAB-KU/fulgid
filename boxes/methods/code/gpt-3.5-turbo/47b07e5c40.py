# Initialize the boxes
boxes = {
    0: ['car', 'cash', 'map'],
    1: [],
    2: ['hat', 'pot', 'shoe'],
    3: ['book'],
    4: ['glass'],
    5: ['engine', 'jacket'],
    6: ['camera', 'dress'],
}

# Define the moves
moves = [
    (None, 3, 'clock'),     # Put the clock into Box 3
    (4, None, 'glass'),     # Remove the glass from Box 4
    (None, 5, 'magazine'),  # Put the magazine into Box 5
    (0, None, 'car'),       # Remove the car from Box 0
    (0, None, 'cash'),      # Remove the cash from Box 0
    (0, None, 'map'),       # Remove the map from Box 0
    (5, None, 'jacket'),    # Remove the jacket from Box 5
    (3, None, 'clock'),     # Remove the clock from Box 3
    (None, 0, 'picture'),   # Put the picture into Box 0
    (5, None, 'magazine'),  # Remove the magazine from Box 5
    (None, 0, 'bomb'),      # Put the bomb into Box 0
    (3, None, 'cross'),     # Remove the cross from Box 3
    (0, 1, 'bomb'),         # Move the bomb from Box 0 to Box 1
    (0, 1, 'picture')       # Move the picture from Box 0 to Box 1
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