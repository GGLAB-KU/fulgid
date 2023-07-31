# Initialize the boxes
boxes = {
    0: ['bell', 'cigarette', 'tape'],
    1: ['picture', 'string', 'suit'],
    2: ['brick', 'computer'],
    3: ['beer', 'cream', 'fan'],
    4: [],
    5: ['plate'],
    6: [],
}

# Define the moves
moves = [
    (3, None, 'cream'),       # Remove the cream from Box 3
    (1, None, 'picture'),     # Remove the picture from Box 1
    (1, None, 'string'),      # Remove the string from Box 1
    (1, 2, 'suit'),           # Move the suit from Box 1 to Box 2
    (5, 6, 'plate'),          # Move the plate from Box 5 to Box 6
    (None, 3, 'rock'),        # Put the rock into Box 3
    (2, 1, 'computer'),       # Move the computer from Box 2 to Box 1
    (6, None, 'plate')        # Remove the plate from Box 6
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