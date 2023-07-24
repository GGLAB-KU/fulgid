# Initialize the boxes
boxes = {
    0: ['letter', 'stone'],
    1: [],
    2: ['bell', 'cash'],
    3: ['bowl', 'seed', 'tea'],
    4: ['cup'],
    5: ['knife', 'ring'],
    6: [],
}

# Define the moves
moves = [
    (2, None, 'bell'),   # Remove the bell from Box 2
    (2, None, 'cash')    # Remove the cash from Box 2
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