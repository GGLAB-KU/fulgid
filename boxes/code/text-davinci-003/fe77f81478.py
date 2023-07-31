# Initialize the boxes
boxes = {
    0: [],
    1: ['cash', 'hat'],
    2: ['car', 'phone', 'sheet'],
    3: ['crown'],
    4: ['document', 'medicine'],
    5: ['jacket', 'machine', 'tape'],
    6: ['cream'],
}

# Define the moves
moves = [
    (2, None, 'car'),       # Remove the car from Box 2
    (2, None, 'sheet'),     # Remove the sheet from Box 2
    (None, 4, 'picture'),   # Put the picture into Box 4
    (None, 3, 'boat'),      # Put the boat into Box 3
    (6, 1, 'cream'),        # Move the cream from Box 6 to Box 1
    (2, 6, 'phone'),        # Move the phone from Box 2 to Box 6
    (None, 2, 'boot'),      # Put the boot into Box 2
    (None, 2, 'bottle'),    # Put the bottle into Box 2
    (None, 2, 'watch'),     # Put the watch into Box 2
    (1, None, 'cash'),      # Remove the cash from Box 1
    (1, None, 'cream'),     # Remove the cream from Box 1
    (1, None, 'hat'),       # Remove the hat from Box 1
    (2, None, 'bottle'),    # Remove the bottle from Box 2
    (3, None, 'boat'),      # Remove the boat from Box 3
    (4, None, 'document'),  # Remove the document from Box 4
    (4, None, 'medicine'),  # Remove the medicine from Box 4
    (None, 3, 'rose'),      # Put the rose into Box 3
    (6, 0, 'phone')         # Move the phone from Box 6 to Box 0
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