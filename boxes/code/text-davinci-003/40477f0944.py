# Initialize the boxes
boxes = {
    0: ['hat', 'seed'],
    1: ['drink'],
    2: ['block'],
    3: ['brain', 'fan', 'shoe'],
    4: ['pot'],
    5: ['file', 'rock', 'train'],
    6: ['bone', 'tape'],
}

# Define the moves
moves = [
    (2, None, 'block'),    # Remove the block from Box 2
    (0, 2, 'hat'),         # Move the hat from Box 0 to Box 2
    (6, None, 'tape'),     # Remove the tape from Box 6
    (None, 2, 'milk'),     # Put the milk into Box 2
    (2, None, 'milk'),     # Remove the milk from Box 2
    (None, 1, 'ball')      # Put the ball into Box 1
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