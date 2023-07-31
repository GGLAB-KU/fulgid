# Initialize the boxes
boxes = {
    0: ['bowl', 'drug'],
    1: ['crown', 'leaf', 'newspaper'],
    2: ['dish', 'painting'],
    3: ['watch'],
    4: ['boot', 'document', 'map'],
    5: ['bill', 'seed', 'wire'],
    6: ['cigarette', 'fan'],
}

# Define the moves
moves = [
    (1, None, 'crown'),        # Remove the crown from Box 1
    (1, None, 'leaf'),         # Remove the leaf from Box 1
    (1, None, 'newspaper'),    # Remove the newspaper from Box 1
    (2, 3, 'painting'),        # Move the painting from Box 2 to Box 3
    (5, 1, 'bill'),            # Move the bill from Box 5 to Box 1
    (4, None, 'boot'),         # Remove the boot from Box 4
    (4, None, 'document'),     # Remove the document from Box 4
    (6, 4, 'newspaper'),       # Put the newspaper into Box 6
    (None, 4, 'bomb'),         # Put the bomb into Box 4
    (None, 4, 'brain'),        # Put the brain into Box 4
    (None, 1, 'rose'),         # Put the rose into Box 1
    (4, None, 'bomb'),         # Remove the bomb from Box 4
    (4, None, 'brain'),        # Remove the brain from Box 4
    (6, 4, 'cigarette'),       # Move the cigarette from Box 6 to Box 4
    (6, 4, 'newspaper'),       # Move the newspaper from Box 6 to Box 4
    (5, None, 'wire'),         # Remove the wire from Box 5
    (4, None, 'newspaper'),    # Remove the newspaper from Box 4
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