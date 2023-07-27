# Initialize the boxes
boxes = {
    0: ['cheese', 'guitar', 'string'],
    1: [],
    2: ['brick', 'clock', 'tea'],
    3: ['drug'],
    4: ['apple'],
    5: [],
    6: ['newspaper'],
}

# Define the moves
moves = [
    (None, 3, 'milk'),    # Put the milk into Box 3
    (2, None, 'tea'),     # Remove the tea from Box 2
    (0, 1, 'string'),     # Move the string from Box 0 to Box 1
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