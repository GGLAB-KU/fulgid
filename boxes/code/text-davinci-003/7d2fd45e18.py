# Initialize the boxes
boxes = {
    0: ['cash', 'shoe'],
    1: ['magazine', 'pot'],
    2: ['egg', 'fan', 'letter'],
    3: ['coffee', 'painting', 'ticket'],
    4: ['bomb'],
    5: ['bottle', 'machine'],
    6: ['ball', 'camera', 'picture'],
}

# Define the moves
moves = [
    (1, None, 'pot'),       # Remove the pot from Box 1
    (0, None, 'cash'),      # Remove the cash from Box 0
    (0, None, 'shoe'),      # Remove the shoe from Box 0
    (6, 4, 'ball'),         # Move the ball from Box 6 to Box 4
    (6, 4, 'picture'),      # Move the picture from Box 6 to Box 4
    (2, None, 'letter'),    # Remove the letter from Box 2
    (6, None, 'camera'),    # Remove the camera from Box 6
    (None, 2, 'branch'),    # Put the branch into Box 2
    (5, None, 'bottle'),    # Remove the bottle from Box 5
    (5, None, 'machine'),   # Remove the machine from Box 5
    (3, None, 'coffee'),    # Remove the coffee from Box 3
    (3, None, 'ticket'),    # Remove the ticket from Box 3
    (4, None, 'picture')    # Remove the picture from Box 4
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