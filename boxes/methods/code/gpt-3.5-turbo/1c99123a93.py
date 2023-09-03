# Initialize the boxes
boxes = {
    0: ['bus', 'game', 'plate'],
    1: ['fig'],
    2: ['letter', 'machine', 'rock'],
    3: ['pot'],
    4: [],
    5: ['plant'],
    6: ['coffee', 'egg', 'plane'],
}

# Define the moves
moves = [
    (3, 5, 'pot'),       # Move the pot from Box 3 to Box 5
    (None, 3, 'coat'),   # Put the coat into Box 3
    (None, 5, 'branch'), # Put the branch into Box 5
    (None, 4, 'camera'), # Put the camera into Box 4
    (5, None, 'branch'), # Remove the branch from Box 5
    (4, None, 'camera'), # Remove the camera from Box 4
    (0, None, 'game'),   # Remove the game from Box 0
    (3, 1, 'coat'),      # Move the coat from Box 3 to Box 1
    (0, 4, 'bus'),       # Move the bus from Box 0 to Box 4
    (0, 4, 'plate'),     # Move the plate from Box 0 to Box 4
    (4, None, 'bus'),    # Remove the bus from Box 4
    (4, None, 'plate'),  # Remove the plate from Box 4
    (2, None, 'letter'), # Remove the letter from Box 2
    (2, None, 'machine'),# Remove the machine from Box 2
    (2, None, 'rock'),   # Remove the rock from Box 2
    (1, 2, 'fig'),       # Move the fig from Box 1 to Box 2
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