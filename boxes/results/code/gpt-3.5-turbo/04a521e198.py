# Initialize the boxes
boxes = {
    0: ['bus', 'coat'],
    1: [],
    2: ['coffee'],
    3: ['file'],
    4: ['watch'],
    5: ['meat', 'tie', 'train'],
    6: ['medicine', 'picture', 'television'],
}

# Define the moves
moves = [
    (4, None, 'watch'),     # Remove the watch from Box 4
    (None, 4, 'game'),      # Put the game into Box 4
    (None, 2, 'cup'),       # Put the cup into Box 2
    (4, None, 'game'),      # Remove the game from Box 4
    (0, None, 'bus'),       # Remove the bus from Box 0
    (0, None, 'coat'),      # Remove the coat from Box 0
    (2, 4, 'coffee'),       # Move the coffee from Box 2 to Box 4
    (2, 4, 'cup'),          # Move the cup from Box 2 to Box 4
    (4, 2, 'cup')           # Move the cup from Box 4 to Box 2
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