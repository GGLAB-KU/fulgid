# Initialize the boxes
boxes = {
    0: ['bus', 'wheel'],
    1: ['cross'],
    2: ['note', 'shirt'],
    3: ['suit', 'tie'],
    4: ['brain', 'string'],
    5: ['cash', 'crown'],
    6: ['cream', 'seed'],
}

# Define the moves
moves = [
    (3, 6, 'tie'),         # Move the tie from Box 3 to Box 6
    (2, None, 'note'),     # Remove the note from Box 2
    (None, 4, 'jacket'),   # Put the jacket into Box 4
    (4, 0, 'brain'),       # Move the brain from Box 4 to Box 0
    (3, None, 'suit'),     # Remove the suit from Box 3
    (None, 3, 'bill'),     # Put the bill into Box 3
    (None, 3, 'card'),     # Put the card into Box 3
    (None, 3, 'drink'),    # Put the drink into Box 3
    (0, 4, 'brain'),       # Move the brain from Box 0 to Box 4
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