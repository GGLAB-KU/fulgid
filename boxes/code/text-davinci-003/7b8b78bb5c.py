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
    (None, 1, 'clock'),     # Put the clock into Box 1
    (5, None, 'note'),      # Remove the note from Box 5
    (None, 0, 'bowl'),      # Put the bowl into Box 0
    (None, 0, 'drug'),      # Put the drug into Box 0
    (1, None, 'clock'),     # Remove the clock from Box 1
    (None, 6, 'branch'),    # Put the branch into Box 6
    (2, None, 'plant'),     # Remove the plant from Box 2
    (2, None, 'tea'),       # Remove the tea from Box 2
    (None, 5, 'bill'),      # Put the bill into Box 5
    (5, None, 'bill'),      # Remove the bill from Box 5
    (4, None, 'file'),      # Remove the file from Box 4
    (4, None, 'flower'),    # Remove the flower from Box 4
    (4, None, 'plate'),     # Remove the plate from Box 4
    (None, 5, 'disk'),      # Put the disk into Box 5
    (None, 5, 'shirt'),     # Put the shirt into Box 5
    (None, 4, 'boat'),      # Put the boat into Box 4
    (None, 4, 'milk')       # Put the milk into Box 4
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