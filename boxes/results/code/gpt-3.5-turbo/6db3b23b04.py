# Initialize the boxes
boxes = {
    0: ['wire'],
    1: ['bag', 'boat', 'leaf'],
    2: ['seed'],
    3: ['chemical', 'file'],
    4: ['painting'],
    5: ['watch'],
    6: ['glass'],
}

# Define the moves
moves = [
    (6, 3, 'glass'),        # Move the glass from Box 6 to Box 3
    (None, 4, 'clock'),     # Put the clock into Box 4
    (None, 4, 'letter'),    # Put the letter into Box 4
    (2, None, 'coffee'),    # Put the coffee into Box 2
    (2, 0, 'coffee'),       # Move the coffee from Box 2 to Box 0
    (3, None, 'chemical'),  # Remove the chemical from Box 3
    (3, None, 'file'),      # Remove the file from Box 3
    (3, None, 'glass'),     # Remove the glass from Box 3
    (5, None, 'watch'),     # Remove the watch from Box 5
    (0, 2, 'wire'),         # Move the wire from Box 0 to Box 2
    (None, 3, 'jacket'),    # Put the jacket into Box 3
    (None, 6, 'disk'),      # Put the disk into Box 6
    (4, 0, 'letter'),       # Move the letter from Box 4 to Box 0
    (4, 0, 'painting')      # Move the painting from Box 4 to Box 0
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