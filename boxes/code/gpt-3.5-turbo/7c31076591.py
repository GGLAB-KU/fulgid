# Initialize the boxes
boxes = {
    0: ['magazine', 'newspaper', 'painting'],
    1: ['bowl', 'rock'],
    2: ['flower'],
    3: ['guitar', 'pipe'],
    4: ['brick', 'drink', 'phone'],
    5: ['apple', 'hat', 'letter'],
    6: [],
}

# Define the moves
moves = [
    (1, 6, 'bowl'),         # Move the bowl from Box 1 to Box 6
    (1, 6, 'rock'),         # Move the rock from Box 1 to Box 6
    (2, None, 'flower'),    # Remove the flower from Box 2
    (0, None, 'magazine'),  # Remove the magazine from Box 0
    (0, None, 'newspaper'), # Remove the newspaper from Box 0
    (0, None, 'painting'),  # Remove the painting from Box 0
    (3, None, 'guitar'),    # Remove the guitar from Box 3
    (3, None, 'pipe'),      # Remove the pipe from Box 3
    (4, None, 'brick'),     # Remove the brick from Box 4
    (4, None, 'drink'),     # Remove the drink from Box 4
    (1, None, 'dress'),     # Put the dress into Box 1
    (1, 3, 'dress'),        # Move the dress from Box 1 to Box 3
    (4, 3, 'phone'),        # Move the phone from Box 4 to Box 3
    (None, 3, 'radio'),     # Put the radio into Box 3
    (5, 0, 'apple'),        # Move the apple from Box 5 to Box 0
    (5, 0, 'hat'),          # Move the hat from Box 5 to Box 0
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