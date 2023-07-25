# Initialize the boxes
boxes = {
    0: ['block'],
    1: ['card', 'paper'],
    2: [],
    3: ['meat'],
    4: ['suit'],
    5: ['fish', 'wheel'],
    6: [],
}

# Define the moves
moves = [
    (None, 4, 'pipe'),       # Put the pipe into Box 4
    (None, 2, 'ring'),       # Put the ring into Box 2
    (3, 4, 'meat'),          # Move the meat from Box 3 to Box 4
    (4, 2, 'suit'),          # Move the suit from Box 4 to Box 2
    (0, None, 'block'),      # Remove the block from Box 0
    (2, None, 'ring'),       # Remove the ring from Box 2
    (2, None, 'suit'),       # Remove the suit from Box 2
    (4, None, 'meat'),       # Remove the meat from Box 4
    (1, 4, 'paper'),         # Move the paper from Box 1 to Box 4
    (5, None, 'wheel'),      # Remove the wheel from Box 5
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