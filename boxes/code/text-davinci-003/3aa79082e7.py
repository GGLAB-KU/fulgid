# Initialize the boxes
boxes = {
    0: ['cigarette'],
    1: ['shell'],
    2: ['letter'],
    3: [],
    4: ['dress', 'shoe', 'tea'],
    5: ['bomb'],
    6: ['camera', 'hat', 'painting'],
}

# Define the moves
moves = [
    (4, None, 'tea'),       # Remove the tea from Box 4
    (5, 2, 'bomb'),         # Move the bomb from Box 5 to Box 2
    (2, None, 'bomb'),      # Remove the bomb from Box 2
    (2, None, 'letter'),    # Remove the letter from Box 2
    (1, None, 'shell'),     # Remove the shell from Box 1
    (0, None, 'cigarette'), # Remove the cigarette from Box 0
    (6, None, 'camera'),    # Remove the camera from Box 6
    (6, None, 'hat'),       # Remove the hat from Box 6
    (None, 3, 'milk')       # Put the milk into Box 3
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