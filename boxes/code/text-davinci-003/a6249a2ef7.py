# Initialize the boxes
boxes = {
    0: ['camera', 'fan', 'note'],
    1: ['leaf', 'plate'],
    2: ['mirror'],
    3: ['drug'],
    4: ['coffee', 'dress'],
    5: ['key', 'pipe'],
    6: ['egg', 'hat'],
}

# Define the moves
moves = [
    (3, None, 'drug'),       # Remove the drug from Box 3
    (2, None, 'mirror'),     # Remove the mirror from Box 2
    (None, 3, 'ticket'),     # Put the ticket into Box 3
    (1, 3, 'leaf'),          # Move the leaf from Box 1 to Box 3
    (1, 3, 'plate'),         # Move the plate from Box 1 to Box 3
    (None, 6, 'magazine'),   # Put the magazine into Box 6
    (3, None, 'ticket'),     # Remove the ticket from Box 3
    (5, 4, 'key'),           # Move the key from Box 5 to Box 4
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