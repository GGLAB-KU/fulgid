# Initialize the boxes
boxes = {
    0: ['document'],
    1: ['dress', 'radio'],
    2: ['suit'],
    3: ['bill'],
    4: ['pipe'],
    5: ['cup', 'magazine', 'plant'],
    6: [],
}

# Define the moves
moves = [
    (None, 0, 'shell'),   # Put the shell into Box 0
    (None, 0, 'wheel'),   # Put the wheel into Box 0
    (2, None, 'suit'),    # Remove the suit from Box 2
    (4, None, 'pipe'),    # Remove the pipe from Box 4
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