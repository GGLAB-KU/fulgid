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
    (None, 0, 'shell'),     # Put the shell into Box 0
    (None, 0, 'wheel'),     # Put the wheel into Box 0
    (2, None, 'suit'),      # Remove the suit from Box 2
    (4, None, 'pipe'),      # Remove the pipe from Box 4
    (1, None, 'radio'),     # Remove the radio from Box 1
    (None, 4, 'crown'),     # Put the crown into Box 4
    (None, 4, 'note'),      # Put the note into Box 4
    (1, None, 'dress'),     # Remove the dress from Box 1
    (None, 4, 'gift'),      # Put the gift into Box 4
    (4, 1, 'crown'),        # Move the crown from Box 4 to Box 1
    (4, 1, 'gift'),         # Move the gift from Box 4 to Box 1
    (4, 1, 'note'),         # Move the note from Box 4 to Box 1
    (5, None, 'magazine'),  # Remove the magazine from Box 5
    (5, None, 'plant'),     # Remove the plant from Box 5
    (3, None, 'bill'),      # Remove the bill from Box 3
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