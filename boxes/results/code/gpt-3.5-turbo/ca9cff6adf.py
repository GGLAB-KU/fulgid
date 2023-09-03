# Initialize the boxes
boxes = {
    0: ['plate'],
    1: [],
    2: ['string', 'tape'],
    3: ['engine', 'glass'],
    4: ['block', 'map'],
    5: ['brick', 'bus'],
    6: ['bill', 'cream', 'phone'],
}

# Define the moves
moves = [
    (3, None, 'glass'),     # Remove the glass from Box 3
    (5, 0, 'brick'),        # Move the brick from Box 5 to Box 0
    (5, 0, 'bus'),          # Move the bus from Box 5 to Box 0
    (3, None, 'engine'),    # Remove the engine from Box 3
    (4, None, 'block'),     # Remove the block from Box 4
    (0, None, 'bus'),       # Remove the bus from Box 0
    (0, None, 'plate'),     # Remove the plate from Box 0
    (4, 5, 'block'),        # Put the block into Box 5
    (4, None, 'map'),       # Remove the map from Box 4
    (6, None, 'cream'),     # Remove the cream from Box 6
    (6, None, 'phone'),     # Remove the phone from Box 6
    (6, 2, 'bill'),         # Move the bill from Box 6 to Box 2
    (2, None, 'bill'),      # Remove the bill from Box 2
    (2, 4, 'string'),       # Move the string from Box 2 to Box 4
    (0, None, 'brick'),     # Remove the brick from Box 0
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