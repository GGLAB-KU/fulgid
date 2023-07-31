# Initialize the boxes
boxes = {
    0: [],
    1: ['coat', 'drug'],
    2: [],
    3: [],
    4: [],
    5: ['computer', 'cross', 'pipe'],
    6: ['glass'],
}

# Define the moves
moves = [
    (5, None, 'computer'),  # Remove the computer from Box 5
    (5, None, 'cross'),     # Remove the cross from Box 5
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