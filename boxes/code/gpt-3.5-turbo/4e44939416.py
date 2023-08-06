# Initialize the boxes
boxes = {
    0: ['book', 'brick'],
    1: ['bus', 'crown', 'plant'],
    2: ['apple', 'drug', 'wire'],
    3: ['file'],
    4: ['game'],
    5: ['paper', 'ring'],
    6: ['milk', 'watch'],
}

# Define the moves
moves = [
    (1, None, 'bus'),   # Remove the bus from Box 1
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