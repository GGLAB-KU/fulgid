# Initialize the boxes
boxes = {
    0: ['bus'],
    1: ['bowl', 'dish', 'suit'],
    2: [],
    3: ['pot'],
    4: ['boat', 'egg'],
    5: ['boot', 'drug'],
    6: ['cigarette'],
}

# Define the moves
moves = [
    (1, 2, 'plate'),       # Put the plate into Box 2
    (6, None, 'cigarette'), # Remove the cigarette from Box 6
    (None, 2, 'key'),       # Put the key into Box 2
    (None, 5, 'bill'),      # Put the bill into Box 5
    (2, None, 'key'),       # Remove the key from Box 2
    (2, None, 'plate'),     # Remove the plate from Box 2
    (1, None, 'bowl'),      # Remove the bowl from Box 1
    (1, 2, 'suit'),         # Move the suit from Box 1 to Box 2
    (2, None, 'suit'),      # Remove the suit from Box 2
    (4, None, 'egg'),       # Remove the egg from Box 4
    (0, 2, 'bus'),          # Move the bus from Box 0 to Box 2
    (2, 3, 'bus'),          # Move the bus from Box 2 to Box 3
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