# Initialize the boxes
boxes = {
    0: ['hat'],
    1: ['cream', 'drug'],
    2: ['bottle', 'glass', 'medicine'],
    3: ['document', 'machine', 'mirror'],
    4: ['meat', 'tissue'],
    5: ['file'],
    6: ['key', 'sheet'],
}

# Define the moves
moves = [
    (3, None, 'document'),  # Remove the document from Box 3
    (3, None, 'machine'),   # Remove the machine from Box 3
    (4, 5, 'meat'),         # Move the meat from Box 4 to Box 5
    (4, 5, 'tissue'),       # Move the tissue from Box 4 to Box 5
    (3, None, 'mirror'),    # Remove the mirror from Box 3
    (6, None, 'key'),       # Remove the key from Box 6
    (6, None, 'sheet'),     # Remove the sheet from Box 6
    (0, 6, 'hat'),          # Move the hat from Box 0 to Box 6
    (None, 4, 'knife'),     # Put the knife into Box 4
    (2, 1, 'bottle'),       # Move the bottle from Box 2 to Box 1
    (4, None, 'knife'),     # Remove the knife from Box 4
    (1, 4, 'bottle'),       # Move the bottle from Box 1 to Box 4
    (None, 6, 'note')       # Put the note into Box 6
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