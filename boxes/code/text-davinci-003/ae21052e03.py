# Initialize the boxes
boxes = {
    0: ['radio', 'rock'],
    1: ['bone'],
    2: ['map'],
    3: ['leaf', 'note', 'plate'],
    4: ['tie'],
    5: ['cup', 'sheet'],
    6: ['cross', 'key', 'painting'],
}

# Define the moves
moves = [
    (None, 5, 'boot'),   # Put the boot into Box 5
    (5, None, 'boot'),   # Remove the boot from Box 5
    (4, 0, 'tie'),       # Move the tie from Box 4 to Box 0
    (2, None, 'map'),    # Remove the map from Box 2
    (5, 1, 'cup'),       # Move the cup from Box 5 to Box 1
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