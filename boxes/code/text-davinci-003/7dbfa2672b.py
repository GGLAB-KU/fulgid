# Initialize the boxes
boxes = {
    0: ['document', 'string'],
    1: ['plane', 'stone', 'television'],
    2: ['boot', 'bottle', 'ring'],
    3: ['key', 'medicine'],
    4: ['machine'],
    5: [],
    6: ['dress'],
}

# Define the moves
moves = [
    (4, 3, 'machine'),   # Move the machine from Box 4 to Box 3
    (1, None, 'plane'),  # Remove the plane from Box 1
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