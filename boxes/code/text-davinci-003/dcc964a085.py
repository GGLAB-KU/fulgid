# Initialize the boxes
boxes = {
    0: ['rose'],
    1: ['brick', 'fish', 'shirt'],
    2: ['ball', 'pot', 'watch'],
    3: ['fan', 'suit'],
    4: ['brain', 'egg', 'wheel'],
    5: ['boat', 'drug'],
    6: ['map'],
}

# Define the moves
moves = [
    (None, 3, 'beer'),       # Put the beer into Box 3
    (3, None, 'beer'),       # Remove the beer from Box 3
    (3, None, 'fan'),        # Remove the fan from Box 3
    (3, None, 'suit'),       # Remove the suit from Box 3
    (1, None, 'fish'),       # Remove the fish from Box 1
    (1, None, 'shirt'),      # Remove the shirt from Box 1
    (2, 0, 'ball'),          # Move the ball from Box 2 to Box 0
    (6, None, 'map'),        # Remove the map from Box 6
    (2, None, 'pot'),        # Remove the pot from Box 2
    (None, 6, 'game'),       # Put the game into Box 6
    (None, 6, 'knife'),      # Put the knife into Box 6
    (0, None, 'ball'),       # Remove the ball from Box 0
    (0, None, 'rose'),       # Remove the rose from Box 0
    (2, None, 'watch'),      # Remove the watch from Box 2
    (None, 0, 'computer'),   # Put the computer into Box 0
    (1, None, 'brick')       # Remove the brick from Box 1
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