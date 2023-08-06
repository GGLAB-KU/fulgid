# Initialize the boxes
boxes = {
    0: ['camera', 'fan', 'pot'],
    1: [],
    2: [],
    3: ['train'],
    4: ['clock', 'fig', 'tea'],
    5: ['bill', 'machine', 'wire'],
    6: [],
}

# Define the moves
moves = [
    (0, 1, 'pot'),          # Move the pot from Box 0 to Box 1
    (1, None, 'pot'),       # Remove the pot from Box 1
    (5, 3, 'bill'),         # Move the bill from Box 5 to Box 3
    (5, 3, 'machine'),      # Move the machine from Box 5 to Box 3
    (5, 6, 'wire'),         # Move the wire from Box 5 to Box 6
    (None, 2, 'tissue'),    # Put the tissue into Box 2
    (6, 2, 'wire'),         # Move the wire from Box 6 to Box 2
    (4, 5, 'clock'),        # Move the clock from Box 4 to Box 5
    (4, 5, 'fig'),          # Move the fig from Box 4 to Box 5
    (2, 4, 'tissue'),       # Move the tissue from Box 2 to Box 4
    (2, 4, 'wire'),         # Move the wire from Box 2 to Box 4
    (5, None, 'clock'),     # Remove the clock from Box 5
    (5, None, 'fig')        # Remove the fig from Box 5
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