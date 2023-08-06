# Initialize the boxes
boxes = {
    0: ['bottle'],
    1: [],
    2: ['ball', 'plant', 'tea'],
    3: ['chemical', 'phone'],
    4: ['file', 'flower', 'plate'],
    5: ['meat', 'note'],
    6: ['beer', 'guitar'],
}

# Define the moves
moves = [
    (None, 1, 'clock'),    # Put the clock into Box 1
    (5, None, 'note'),     # Remove the note from Box 5
    (None, 0, 'bowl'),     # Put the bowl into Box 0
    (None, 0, 'drug')      # Put the drug into Box 0
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