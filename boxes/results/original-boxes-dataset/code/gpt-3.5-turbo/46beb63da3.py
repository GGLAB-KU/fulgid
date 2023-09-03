# Initialize the boxes
boxes = {
    0: [],
    1: ['bone'],
    2: ['meat'],
    3: ['car', 'plate', 'stone'],
    4: ['boot', 'fig', 'jacket'],
    5: ['ball', 'creature', 'shirt'],
    6: ['crown', 'glass', 'guitar'],
}

# Define the moves
moves = [
    (3, 0, 'dish'),         # Put the dish into Box 0
    (5, None, 'shirt'),     # Remove the shirt from Box 5
    (1, 2, 'bone'),         # Move the bone from Box 1 to Box 2
    (4, None, 'boot'),      # Remove the boot from Box 4
    (4, None, 'fig'),       # Remove the fig from Box 4
    (None, 1, 'branch'),    # Put the branch into Box 1
    (None, 1, 'document'),  # Put the document into Box 1
    (None, 1, 'file'),      # Put the file into Box 1
    (6, None, 'crown'),     # Remove the crown from Box 6
    (1, None, 'document'),  # Remove the document from Box 1
    (0, 4, 'dish'),         # Move the dish from Box 0 to Box 4
    (4, None, 'dish'),      # Remove the dish from Box 4
    (2, None, 'meat'),      # Remove the meat from Box 2
    (None, 0, 'boat'),      # Put the boat into Box 0
    (3, None, 'stone'),     # Remove the stone from Box 3
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