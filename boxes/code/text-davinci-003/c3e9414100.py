# Initialize the boxes
boxes = {
    0: ['meat'],
    1: ['computer', 'creature', 'drink'],
    2: ['bone', 'cigarette', 'drug'],
    3: [],
    4: ['egg', 'gift', 'radio'],
    5: ['hat', 'milk', 'seed'],
    6: ['plant'],
}

# Define the moves
moves = [
    (1, None, 'drink'),     # Remove the drink from Box 1
    (5, 3, 'hat'),          # Move the hat from Box 5 to Box 3
    (5, 3, 'seed'),         # Move the seed from Box 5 to Box 3
    (6, None, 'plant')      # Remove the plant from Box 6
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