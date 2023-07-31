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
    (5, None, 'plane'),   # Remove the plane from Box 5
    (None, 6, 'machine'), # Put the machine into Box 6
    (6, None, 'machine')  # Remove the machine from Box 6
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