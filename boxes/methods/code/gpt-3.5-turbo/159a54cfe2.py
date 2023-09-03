# Initialize the boxes
boxes = {
    0: [],
    1: ['document'],
    2: ['wheel'],
    3: ['branch'],
    4: ['file'],
    5: ['leaf', 'machine', 'milk'],
    6: ['phone'],
}

# Define the moves
moves = [
    (5, 3, 'leaf'),         # Move the leaf from Box 5 to Box 3
    (1, 6, 'document'),     # Move the document from Box 1 to Box 6
    (4, None, 'file'),      # Remove the file from Box 4
    (5, None, 'machine'),   # Remove the machine from Box 5
    (5, 1, 'milk'),         # Move the milk from Box 5 to Box 1
    (3, 1, 'leaf'),         # Move the leaf from Box 3 to Box 1
    (None, 1, 'ring'),      # Put the ring into Box 1
    (3, 4, 'branch'),       # Move the branch from Box 3 to Box 4
    (6, None, 'phone'),     # Remove the phone from Box 6
    (6, 2, 'document'),     # Move the document from Box 6 to Box 2
    (1, 2, 'ring'),         # Move the ring from Box 1 to Box 2
    (1, 3, 'milk')          # Move the milk from Box 1 to Box 3
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