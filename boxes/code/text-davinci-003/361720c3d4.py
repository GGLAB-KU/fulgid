# Initialize the boxes
boxes = {
    0: ['beer', 'cheese', 'flower'],
    1: ['gift', 'radio', 'tape'],
    2: ['string', 'tie'],
    3: ['picture'],
    4: ['wire'],
    5: ['creature'],
    6: ['brain', 'camera', 'rock'],
}

# Define the moves
moves = [
    (1, 3, 'tape'),     # Move the tape from Box 1 to Box 3
    (2, None, 'string'),    # Remove the string from Box 2
    (3, None, 'picture'),   # Remove the picture from Box 3
    (6, 5, 'rock'),     # Move the rock from Box 6 to Box 5
    (2, 5, 'tie'),      # Move the tie from Box 2 to Box 5
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