# Initialize the boxes
boxes = {
    0: ['book', 'flower', 'shirt'],
    1: ['camera', 'dress', 'jacket'],
    2: ['picture'],
    3: [],
    4: ['string'],
    5: ['tape'],
    6: ['fig'],
}

# Define the moves
moves = [
    (4, None, 'string'),    # Remove the string from Box 4
    (6, None, 'fig'),       # Remove the fig from Box 6
    (1, None, 'dress'),     # Remove the dress from Box 1
    (1, None, 'jacket'),    # Remove the jacket from Box 1
    (0, 3, 'book'),         # Move the book from Box 0 to Box 3
    (0, 4, 'flower'),       # Move the flower from Box 0 to Box 4
    (None, 0, 'egg'),       # Put the egg into Box 0
    (None, 0, 'map'),       # Put the map into Box 0
    (5, 4, 'tape'),         # Move the tape from Box 5 to Box 4
    (None, 4, 'fish')       # Put the fish into Box 4
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