# Initialize the boxes
boxes = {
    0: ['apple'],
    1: ['block', 'document', 'jacket'],
    2: ['machine'],
    3: [],
    4: ['sheet', 'tissue'],
    5: ['egg', 'ice'],
    6: ['mirror', 'plane', 'string'],
}

# Define the moves
moves = [
    (5, None, 'ice'),   # Remove the ice from Box 5
    (0, None, 'apple')  # Remove the apple from Box 0
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