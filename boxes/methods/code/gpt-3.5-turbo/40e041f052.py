# Initialize the boxes
boxes = {
    0: ['picture', 'tape'],
    1: ['engine', 'phone', 'watch'],
    2: ['train'],
    3: ['boot', 'bowl', 'tissue'],
    4: ['cheese', 'document', 'leaf'],
    5: ['machine'],
    6: ['bag'],
}

# Define the moves
moves = [
    (5, None, 'machine'),       # Remove the machine from Box 5
    (0, None, 'picture'),       # Remove the picture from Box 0
    (0, None, 'tape'),          # Remove the tape from Box 0
    (6, 5, 'bag'),              # Move the bag from Box 6 to Box 5
    (1, 2, 'engine'),           # Move the engine from Box 1 to Box 2
    (3, None, 'boot'),          # Remove the boot from Box 3
    (3, None, 'bowl'),          # Remove the bowl from Box 3
    (2, 0, 'train'),            # Move the train from Box 2 to Box 0
    (5, None, 'bag'),           # Remove the bag from Box 5
    (2, None, 'engine'),        # Remove the engine from Box 2
    (1, 5, 'phone'),            # Move the phone from Box 1 to Box 5
    (None, 5, 'branch'),        # Put the branch into Box 5
    (0, 5, 'train'),            # Move the train from Box 0 to Box 5
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