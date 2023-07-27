# Initialize the boxes
boxes = {
    0: ['glass', 'note', 'string'],
    1: ['bus', 'medicine', 'suit'],
    2: ['guitar', 'magazine', 'shirt'],
    3: ['boat', 'camera', 'car'],
    4: ['tape', 'ticket'],
    5: ['fig'],
    6: ['newspaper', 'pipe'],
}

# Define the moves
moves = [
    (None, 6, 'chemical'),     # Put the chemical into Box 6
    (2, None, 'guitar'),        # Remove the guitar from Box 2
    (2, None, 'shirt'),         # Remove the shirt from Box 2
    (5, 2, 'fig'),              # Move the fig from Box 5 to Box 2
    (2, None, 'fig'),           # Remove the fig from Box 2
    (1, None, 'bus'),           # Remove the bus from Box 1
    (1, None, 'suit'),          # Remove the suit from Box 1
    (2, 5, 'magazine'),         # Move the magazine from Box 2 to Box 5
    (3, None, 'camera'),        # Remove the camera from Box 3
    (3, None, 'car'),           # Remove the car from Box 3
    (4, 2, 'ticket'),           # Move the ticket from Box 4 to Box 2
    (5, None, 'magazine'),      # Remove the magazine from Box 5
    (None, 1, 'beer'),          # Put the beer into Box 1
    (None, 5, 'watch')          # Put the watch into Box 5
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