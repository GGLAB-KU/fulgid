# Initialize the boxes
boxes = {
    0: ['beer', 'picture'],
    1: ['string'],
    2: ['cross'],
    3: [],
    4: ['bowl'],
    5: ['drink', 'medicine', 'rose'],
    6: [],
}

# Define the moves
moves = [
    (1, 4, 'string'),       # Move the string from Box 1 to Box 4
    (2, 0, 'cross'),        # Move the cross from Box 2 to Box 0
    (None, 1, 'magazine'),  # Put the magazine into Box 1
    (None, 6, 'boot'),      # Put the boot into Box 6
    (None, 6, 'file'),      # Put the file into Box 6
    (5, None, 'medicine'),  # Remove the medicine from Box 5
    (5, None, 'rose'),      # Remove the rose from Box 5
    (4, 1, 'bowl'),         # Move the bowl from Box 4 to Box 1
    (1, 5, 'bowl'),         # Move the bowl from Box 1 to Box 5
    (6, 4, 'boot'),         # Move the boot from Box 6 to Box 4
    (4, 1, 'boot'),         # Move the boot from Box 4 to Box 1
    (None, 1, 'flower'),    # Put the flower into Box 1
    (5, None, 'bowl'),      # Remove the bowl from Box 5
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