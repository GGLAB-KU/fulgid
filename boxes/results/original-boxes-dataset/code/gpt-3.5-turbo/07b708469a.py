# Initialize the boxes
boxes = {
    0: ['brain', 'newspaper', 'rock'],
    1: ['wheel'],
    2: ['bag', 'block', 'map'],
    3: ['bus', 'gift', 'radio'],
    4: ['plant'],
    5: ['string'],
    6: ['chemical', 'clock'],
}

# Define the moves
moves = [
    (None, 5, 'plane'),     # Put the plane into Box 5
    (1, 4, 'wheel'),        # Move the wheel from Box 1 to Box 4
    (None, 6, 'file'),      # Put the file into Box 6
    (5, None, 'string'),    # Remove the string from Box 5
    (2, 1, 'bag'),          # Move the bag from Box 2 to Box 1
    (3, None, 'bus'),       # Remove the bus from Box 3
    (3, None, 'gift'),      # Remove the gift from Box 3
    (3, None, 'radio'),     # Remove the radio from Box 3
    (5, None, 'plane'),     # Remove the plane from Box 5
    (2, None, 'block'),     # Remove the block from Box 2
    (None, 2, 'watch'),     # Put the watch into Box 2
    (6, 5, 'chemical'),     # Move the chemical from Box 6 to Box 5
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