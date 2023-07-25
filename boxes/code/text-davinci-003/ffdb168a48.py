# Initialize the boxes
boxes = {
    0: ['machine', 'plant', 'tea'],
    1: ['bowl', 'medicine', 'tie'],
    2: [],
    3: ['cake', 'camera', 'note'],
    4: ['boat', 'cheese'],
    5: ['ice'],
    6: ['branch', 'creature', 'drug'],
}

# Define the moves
moves = [
    (0, None, 'machine'),   # Remove the machine from Box 0
    (0, None, 'plant'),     # Remove the plant from Box 0
    (0, None, 'tea'),       # Remove the tea from Box 0
    (4, 0, 'boat'),         # Move the boat from Box 4 to Box 0
    (3, None, 'cake'),      # Remove the cake from Box 3
    (3, None, 'camera'),    # Remove the camera from Box 3
    (2, None, 'game'),      # Put the game into Box 2
    (2, None, 'leaf'),      # Put the leaf into Box 2
    (0, None, 'apple'),     # Put the apple into Box 0
    (0, None, 'sheet'),     # Put the sheet into Box 0
    (0, 5, 'boat'),         # Move the boat from Box 0 to Box 5
    (0, 5, 'sheet'),        # Move the sheet from Box 0 to Box 5
    (None, 4, 'bottle'),    # Put the bottle into Box 4
    (None, 0, 'dish'),      # Put the dish into Box 0
    (2, 0, 'pipe'),         # Put the pipe into Box 2
    (2, None, 'game'),      # Remove the game from Box 2
    (2, None, 'leaf'),      # Remove the leaf from Box 2
    (0, None, 'pipe'),      # Move the pipe from Box 0 to Box 2
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