# Initialize the boxes
boxes = {
    0: [],
    1: ['apple', 'ice'],
    2: ['coat'],
    3: ['cash', 'drug', 'pipe'],
    4: ['bowl', 'cross', 'flower'],
    5: ['painting', 'plane'],
    6: ['tape'],
}

# Define the moves
moves = [
    (None, 0, 'machine'),   # Put the machine into Box 0
    (5, None, 'painting'),   # Remove the painting from Box 5
    (5, None, 'plane'),      # Remove the plane from Box 5
    (3, 4, 'machine'),       # Move the machine from Box 3 to Box 4
    (3, 4, 'cash'),          # Move the cash from Box 3 to Box 4
    (3, 4, 'drug'),          # Move the drug from Box 3 to Box 4
    (3, 4, 'pipe'),          # Move the pipe from Box 3 to Box 4
    (6, 1, 'tape'),          # Move the tape from Box 6 to Box 1
    (1, 3, 'tape'),          # Move the tape from Box 1 to Box 3
    (4, 0, 'cross'),         # Move the cross from Box 4 to Box 0
    (None, 3, 'bell'),       # Put the bell into Box 3
    (None, 3, 'bottle')      # Put the bottle into Box 3
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