# Initialize the boxes
boxes = {
    0: ['brick', 'picture'],
    1: [],
    2: ['pot'],
    3: ['clock'],
    4: ['cup', 'fan', 'game'],
    5: ['ice', 'suit'],
    6: ['painting', 'phone', 'shell'],
}

# Define the moves
moves = [
    (0, None, 'brick'),       # Remove the brick from Box 0
    (0, None, 'picture'),     # Remove the picture from Box 0
    (2, None, 'pot'),         # Remove the pot from Box 2
    (3, None, 'clock'),       # Remove the clock from Box 3
    (4, None, 'cup'),         # Remove the cup from Box 4
    (4, None, 'fan'),         # Remove the fan from Box 4
    (4, None, 'game'),        # Remove the game from Box 4
    (5, None, 'ice'),         # Remove the ice from Box 5
    (5, None, 'suit'),        # Remove the suit from Box 5
    (6, None, 'painting'),    # Remove the painting from Box 6
    (6, None, 'phone'),       # Remove the phone from Box 6
    (6, None, 'shell'),       # Remove the shell from Box 6
    (None, 1, 'brick'),       # Put the brick into Box 1
    (None, 1, 'picture'),     # Put the picture into Box 1
    (None, 1, 'pot'),         # Put the pot into Box 1
    (None, 1, 'clock'),       # Put the clock into Box 1
    (None, 1, 'cup'),         # Put the cup into Box 1
    (None, 1, 'fan'),         # Put the fan into Box 1
    (None, 1, 'game'),        # Put the game into Box 1
    (None, 1, 'ice'),         # Put the ice into Box 1
    (None, 1, 'suit'),        # Put the suit into Box 1
    (None, 1, 'painting'),    # Put the painting into Box 1
    (None, 1, 'phone'),       # Put the phone into Box 1
    (None, 1, 'shell'),       # Put the shell into Box 1
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