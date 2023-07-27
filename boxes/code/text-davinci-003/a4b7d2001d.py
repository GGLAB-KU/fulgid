# Initialize the boxes
boxes = {
    0: ['camera', 'chemical', 'milk'],
    1: [],
    2: ['book', 'radio'],
    3: ['phone'],
    4: ['bus', 'clock', 'computer'],
    5: ['beer'],
    6: [],
}

# Define the moves
moves = [
    (None, 3, 'ring'),    # Put the ring into Box 3
    (2, None, 'book'),    # Remove the book from Box 2
    (2, None, 'radio'),   # Remove the radio from Box 2
    (None, 2, 'sheet'),   # Put the sheet into Box 2
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