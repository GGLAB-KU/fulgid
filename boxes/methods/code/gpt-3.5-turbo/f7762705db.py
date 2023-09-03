# Initialize the boxes
boxes = {
    0: ['bowl', 'glass', 'ring'],
    1: ['computer', 'disk'],
    2: ['ice'],
    3: ['coat', 'file', 'painting'],
    4: ['bomb'],
    5: ['bus', 'magazine', 'meat'],
    6: ['cigarette', 'seed'],
}

# Define the moves
moves = [
    (0, None, 'bowl'),      # Remove the bowl from Box 0
    (0, None, 'glass'),     # Remove the glass from Box 0
    (0, None, 'ring'),      # Remove the ring from Box 0
    (1, 0, 'disk')          # Move the disk from Box 1 to Box 0
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