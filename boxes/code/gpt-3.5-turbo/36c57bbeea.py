# Initialize the boxes
boxes = {
    0: ['bottle', 'cigarette', 'engine'],
    1: ['suit'],
    2: ['fan'],
    3: [],
    4: ['painting'],
    5: ['camera', 'mirror'],
    6: ['branch', 'computer', 'egg'],
}

# Define the moves
moves = [
    (4, 3, 'painting'),     # Move the painting from Box 4 to Box 3
    (3, 5, 'painting'),     # Move the painting from Box 3 to Box 5
    (5, None, 'camera'),    # Remove the camera from Box 5
    (5, None, 'mirror'),    # Remove the mirror from Box 5
    (0, None, 'engine'),    # Remove the engine from Box 0
    (None, 4, 'train'),     # Put the train into Box 4
    (5, 3, 'painting')      # Move the painting from Box 5 to Box 3
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