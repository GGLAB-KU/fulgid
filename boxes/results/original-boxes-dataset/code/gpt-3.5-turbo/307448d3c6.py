# Initialize the boxes
boxes = {
    0: ['chemical', 'disk', 'tie'],
    1: ['shoe'],
    2: ['pot', 'train'],
    3: ['suit'],
    4: ['boat', 'bone', 'fig'],
    5: ['brain', 'game', 'television'],
    6: ['car', 'key', 'pipe'],
}

# Define the moves
moves = [
    (0, None, 'chemical'),    # Remove the chemical from Box 0
    (0, None, 'disk'),        # Remove the disk from Box 0
    (0, None, 'tie'),         # Remove the tie from Box 0
    (None, 3, 'suit'),        # Put the suit into Box 3
    (4, None, 'boat'),        # Remove the boat from Box 4
    (4, None, 'bone'),        # Remove the bone from Box 4
    (4, None, 'fig'),         # Remove the fig from Box 4
    (5, None, 'brain'),       # Remove the brain from Box 5
    (5, None, 'game'),        # Remove the game from Box 5
    (5, None, 'television'),  # Remove the television from Box 5
    (6, None, 'car'),         # Remove the car from Box 6
    (6, None, 'key'),         # Remove the key from Box 6
    (6, None, 'pipe'),        # Remove the pipe from Box 6
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