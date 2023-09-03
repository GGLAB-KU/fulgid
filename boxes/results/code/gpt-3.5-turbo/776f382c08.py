# Initialize the boxes
boxes = {
    0: ['drink', 'plane', 'shell'],
    1: [],
    2: ['cake', 'painting'],
    3: [],
    4: ['bone', 'magazine', 'radio'],
    5: ['chemical', 'plant', 'tape'],
    6: ['flower', 'suit', 'wire'],
}

# Define the moves
moves = [
    (4, 3, 'bone'),         # Move the bone from Box 4 to Box 3
    (5, None, 'chemical'),  # Remove the chemical from Box 5
    (5, None, 'plant'),     # Remove the plant from Box 5
    (3, 4, 'bone'),         # Move the bone from Box 3 to Box 4
    (0, None, 'drink'),     # Remove the drink from Box 0
    (0, None, 'plane'),     # Remove the plane from Box 0
    (0, None, 'shell'),     # Remove the shell from Box 0
    (5, None, 'tape'),      # Remove the tape from Box 5
    (None, 5, 'knife'),     # Put the knife into Box 5
    (None, 5, 'leaf'),      # Put the leaf into Box 5
    (5, None, 'knife')      # Remove the knife from Box 5
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