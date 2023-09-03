# Initialize the boxes
boxes = {
    0: ['pipe'],
    1: ['bone', 'glass', 'wire'],
    2: ['letter', 'radio'],
    3: ['car'],
    4: ['document', 'engine', 'knife'],
    5: ['chemical'],
    6: ['bomb', 'book', 'game'],
}

# Define the moves
moves = [
    (0, None, 'pipe'),       # Remove the pipe from Box 0
    (None, 5, 'brain'),      # Put the brain into Box 5
    (None, 5, 'plane'),      # Put the plane into Box 5
    (2, 3, 'letter'),        # Move the letter from Box 2 to Box 3
    (2, 3, 'radio'),         # Move the radio from Box 2 to Box 3
    (1, None, 'bone'),       # Remove the bone from Box 1
    (1, None, 'wire'),       # Remove the wire from Box 1
    (5, 0, 'brain'),         # Move the brain from Box 5 to Box 0
    (5, 0, 'chemical'),      # Move the chemical from Box 5 to Box 0
    (0, None, 'brain'),      # Remove the brain from Box 0
    (0, None, 'chemical'),   # Remove the chemical from Box 0
    (4, None, 'engine'),     # Remove the engine from Box 4
    (3, None, 'car'),        # Remove the car from Box 3
    (3, None, 'letter'),     # Remove the letter from Box 3
    (5, 0, 'plane'),         # Move the plane from Box 5 to Box 0
    (6, 5, 'bomb'),          # Move the bomb from Box 6 to Box 5
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