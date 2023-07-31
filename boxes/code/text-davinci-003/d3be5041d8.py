# Initialize the boxes
boxes = {
    0: ['ice', 'plant'],
    1: ['cream', 'meat', 'pot'],
    2: ['cigarette', 'crown'],
    3: ['phone', 'shoe'],
    4: ['file', 'map'],
    5: [],
    6: ['car'],
}

# Define the moves
moves = [
    (6, None, 'car'),        # Remove the car from Box 6
    (0, None, 'plant'),      # Remove the plant from Box 0
    (0, 4, 'ice'),           # Move the ice from Box 0 to Box 4
    (2, 0, 'crown'),         # Move the crown from Box 2 to Box 0
    (2, 0, 'cigarette'),     # Move the cigarette from Box 2 to Box 0
    (None, 6, 'beer'),       # Put the beer into Box 6
    (3, None, 'phone'),      # Remove the phone from Box 3
    (None, 0, 'pipe'),       # Put the pipe into Box 0
    (None, 5, 'bread'),      # Put the bread into Box 5
    (4, None, 'ice'),        # Remove the ice from Box 4
    (4, None, 'file')        # Remove the file from Box 4
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