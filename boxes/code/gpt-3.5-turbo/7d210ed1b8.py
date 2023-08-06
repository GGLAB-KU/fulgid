# Initialize the boxes
boxes = {
    0: ['chemical', 'drink'],
    1: ['camera', 'meat'],
    2: ['bill', 'brick', 'guitar'],
    3: ['brain', 'dish', 'ring'],
    4: ['newspaper', 'plant', 'tape'],
    5: [],
    6: ['letter', 'tie'],
}

# Define the moves
moves = [
    (None, 6, 'egg'),       # Put the egg into Box 6
    (3, None, 'brain'),     # Remove the brain from Box 3
    (3, None, 'dish'),      # Remove the dish from Box 3
    (3, None, 'ring'),      # Remove the ring from Box 3
    (1, 0, 'camera'),       # Move the camera from Box 1 to Box 0
    (4, None, 'plant'),     # Remove the plant from Box 4
    (4, None, 'tape'),      # Remove the tape from Box 4
    (1, None, 'meat'),      # Remove the meat from Box 1
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