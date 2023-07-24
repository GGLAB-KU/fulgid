# Initialize the boxes
boxes = {
    0: [],
    1: [],
    2: ['tissue'],
    3: [],
    4: [],
    5: ['cup', 'radio'],
    6: ['cake', 'pipe', 'ticket'],
}

# Define the moves
moves = [
    (5, 2, 'cup'),     # Move the cup from Box 5 to Box 2
    (5, 2, 'radio'),   # Move the radio from Box 5 to Box 2
    (None, 3, 'block'),   # Put the block into Box 3
    (None, 3, 'car'),     # Put the car into Box 3
    (3, 4, 'car'),     # Move the car from Box 3 to Box 4
    (6, 0, 'ticket'),  # Move the ticket from Box 6 to Box 0
    (2, None, 'radio'),   # Remove the radio from Box 2
    (6, 1, 'cake'),    # Move the cake from Box 6 to Box 1
    (6, 1, 'pipe'),    # Move the pipe from Box 6 to Box 1
    (1, None, 'cake'),    # Remove the cake from Box 1
    (3, None, 'block'),   # Remove the block from Box 3
    (2, None, 'cup'),     # Remove the cup from Box 2
    (2, None, 'tissue'),  # Remove the tissue from Box 2
    (4, None, 'car'),     # Remove the car from Box 4
    (1, None, 'pipe'),    # Remove the pipe from Box 1
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