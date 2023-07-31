# Initialize the boxes
boxes = {
    0: ['magazine', 'painting'],
    1: ['cross'],
    2: ['camera', 'cup'],
    3: ['bone', 'wheel'],
    4: ['cheese', 'disk', 'milk'],
    5: ['brain', 'document', 'picture'],
    6: ['glass'],
}

# Define the moves
moves = [
    (None, 3, 'leaf'),       # Put the leaf into Box 3
    (None, 6, 'coat'),       # Put the coat into Box 6
    (None, 6, 'plate'),      # Put the plate into Box 6
    (2, 1, 'cup'),           # Move the cup from Box 2 to Box 1
    (2, None, 'camera'),     # Remove the camera from Box 2
    (3, None, 'bone'),       # Remove the bone from Box 3
    (3, None, 'leaf'),       # Remove the leaf from Box 3
    (1, 2, 'cross'),         # Move the cross from Box 1 to Box 2
    (1, 2, 'cup'),           # Move the cup from Box 1 to Box 2
    (6, None, 'plate'),      # Remove the plate from Box 6
    (3, None, 'wheel'),      # Remove the wheel from Box 3
    (2, None, 'cross'),      # Remove the cross from Box 2
    (5, 2, 'brain'),         # Move the brain from Box 5 to Box 2
    (5, 2, 'picture'),       # Move the picture from Box 5 to Box 2
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