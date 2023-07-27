# Initialize the boxes
boxes = {
    0: ['map', 'television', 'wire'],
    1: ['bottle', 'coat'],
    2: ['boot', 'drink', 'fan'],
    3: ['dress'],
    4: ['plant'],
    5: ['egg', 'medicine'],
    6: [],
}

# Define the moves
moves = [
    (3, None, 'dress'),  # Remove the dress from Box 3
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