# Initialize the boxes
boxes = {
    0: ['chemical', 'milk'],
    1: ['beer', 'bottle'],
    2: ['camera'],
    3: ['drink'],
    4: ['plant'],
    5: ['machine'],
    6: ['watch'],
}

# Define the moves
moves = [
    (None, 5, 'ice'),       # Put the ice into Box 5
    (5, None, 'ice'),       # Remove the ice from Box 5
    (0, None, 'milk'),      # Remove the milk from Box 0
    (0, 2, 'chemical'),     # Move the chemical from Box 0 to Box 2
    (5, 6, 'machine'),      # Move the machine from Box 5 to Box 6
    (None, 0, 'block'),     # Put the block into Box 0
    (None, 0, 'pipe'),      # Put the pipe into Box 0
    (2, None, 'camera'),    # Remove the camera from Box 2
    (0, None, 'block'),     # Remove the block from Box 0
    (0, None, 'pipe'),      # Remove the pipe from Box 0
    (None, 0, 'paper'),     # Put the paper into Box 0
    (2, None, 'chemical'),  # Remove the chemical from Box 2
    (None, 2, 'plane')      # Put the plane into Box 2
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