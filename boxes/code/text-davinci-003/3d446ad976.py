# Initialize the boxes
boxes = {
    0: ['brain'],
    1: ['car', 'magazine', 'ring'],
    2: ['camera', 'engine'],
    3: ['bottle', 'picture', 'stone'],
    4: [],
    5: ['bag', 'computer', 'guitar'],
    6: [],
}

# Define the moves
moves = [
    (5, None, 'computer'),   # Remove the computer from Box 5
    (3, None, 'bottle'),     # Remove the bottle from Box 3
    (3, None, 'picture'),    # Remove the picture from Box 3
    (3, None, 'stone'),      # Remove the stone from Box 3
    (None, 3, 'machine'),    # Put the machine into Box 3
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