# Initialize the boxes
boxes = {
    0: [],
    1: ['brick', 'ice', 'suit'],
    2: ['book', 'dish', 'fig'],
    3: [],
    4: [],
    5: ['painting', 'train'],
    6: ['camera', 'tape', 'tie'],
}

# Define the moves
moves = [
    (6, 5, 'tape'),         # Move the tape from Box 6 to Box 5
    (None, 3, 'ticket'),    # Put the ticket into Box 3
    (None, 0, 'jacket'),    # Put the jacket into Box 0
    (1, None, 'brick'),     # Remove the brick from Box 1
    (2, None, 'book'),      # Remove the book from Box 2
    (2, None, 'dish'),      # Remove the dish from Box 2
    (2, None, 'fig'),       # Remove the fig from Box 2
    (5, None, 'train'),     # Remove the train from Box 5
    (None, 2, 'plant'),     # Put the plant into Box 2
    (2, 1, 'plant'),        # Move the plant from Box 2 to Box 1
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