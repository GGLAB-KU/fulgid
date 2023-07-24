# Initialize the boxes
boxes = {
    0: ['bottle', 'pot', 'tea'],
    1: [],
    2: ['bone', 'camera', 'dress'],
    3: ['apple', 'bill', 'cake'],
    4: ['brain', 'mirror', 'radio'],
    5: [],
    6: ['engine'],
}

# Define the moves
moves = [
    (0, 1, 'coffee'),   # Put the coffee into Box 1
    (1, None, 'coffee')  # Remove the coffee from Box 1
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