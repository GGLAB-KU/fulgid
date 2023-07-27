# Initialize the boxes
boxes = {
    0: ['rock'],
    1: ['bill', 'flower', 'guitar'],
    2: ['branch', 'medicine', 'mirror'],
    3: ['bowl', 'map'],
    4: ['ball', 'boat', 'bread'],
    5: ['glass', 'painting'],
    6: ['card', 'crown', 'shirt'],
}

# Define the moves
moves = [
    (0, None, 'rock'),         # Remove the rock from Box 0
    (2, None, 'branch'),       # Remove the branch from Box 2
    (2, None, 'medicine'),     # Remove the medicine from Box 2
    (2, None, 'mirror'),       # Remove the mirror from Box 2
    (3, 0, 'bowl'),            # Move the bowl from Box 3 to Box 0
    (None, 0, 'plane'),        # Put the plane into Box 0
    (3, None, 'map'),          # Remove the map from Box 3
    (0, None, 'plane'),        # Remove the plane from Box 0
    (0, None, 'bowl'),         # Remove the bowl from Box 0
    (2, None, 'brick'),        # Put the brick into Box 2
    (None, 3, 'document'),     # Put the document into Box 3
    (None, 3, 'note'),         # Put the note into Box 3
    (1, 2, 'bill'),            # Move the bill from Box 1 to Box 2
    (3, 0, 'note'),            # Move the note from Box 3 to Box 0
    (3, None, 'document'),     # Remove the document from Box 3
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