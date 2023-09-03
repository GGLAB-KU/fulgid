# Initialize the boxes
boxes = {
    0: ['beer', 'engine'],
    1: ['bag', 'disk', 'fan'],
    2: ['phone', 'shoe'],
    3: ['string'],
    4: ['ball', 'card'],
    5: ['egg', 'fig', 'milk'],
    6: ['jacket'],
}

# Define the moves
moves = [
    (4, 3, 'ball'),         # Move the ball from Box 4 to Box 3
    (3, None, 'ball'),      # Remove the ball from Box 3
    (None, 2, 'sheet'),     # Put the sheet into Box 2
    (0, 3, 'engine'),       # Move the engine from Box 0 to Box 3
    (6, None, 'jacket'),    # Remove the jacket from Box 6
    (4, 3, 'card'),         # Move the card from Box 4 to Box 3
    (None, 6, 'bone'),      # Put the bone into Box 6
    (None, 6, 'jacket'),    # Put the jacket into Box 6
    (1, None, 'fan'),       # Remove the fan from Box 1
    (2, None, 'phone'),     # Remove the phone from Box 2
    (2, None, 'sheet'),     # Remove the sheet from Box 2
    (1, 2, 'bag'),          # Move the bag from Box 1 to Box 2
    (3, 1, 'card'),         # Move the card from Box 3 to Box 1
    (3, None, 'engine'),    # Remove the engine from Box 3
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