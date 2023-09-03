# Initialize the boxes
boxes = {
    0: ['computer', 'plate'],
    1: ['tissue'],
    2: ['cash', 'pipe'],
    3: ['beer'],
    4: [],
    5: ['meat'],
    6: ['knife', 'stone', 'tape'],
}

# Define the moves
moves = [
    (6, None, 'tape'),       # Remove the tape from Box 6
    (None, 5, 'rock'),       # Put the rock into Box 5
    (None, 5, 'wheel'),      # Put the wheel into Box 5
    (None, 2, 'coat'),       # Put the coat into Box 2
    (6, None, 'knife'),      # Remove the knife from Box 6
    (1, None, 'tissue'),     # Remove the tissue from Box 1
    (None, 0, 'suit'),       # Put the suit into Box 0
    (3, 6, 'beer'),          # Move the beer from Box 3 to Box 6
    (None, 6, 'milk'),       # Put the milk into Box 6
    (2, None, 'coat'),       # Remove the coat from Box 2
    (None, 4, 'leaf'),       # Put the leaf into Box 4
    (None, 4, 'picture'),    # Put the picture into Box 4
    (6, None, 'beer'),       # Remove the beer from Box 6
    (6, None, 'stone')       # Remove the stone from Box 6
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