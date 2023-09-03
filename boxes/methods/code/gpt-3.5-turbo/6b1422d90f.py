# Initialize the boxes
boxes = {
    0: ['key', 'magazine'],
    1: ['shell'],
    2: ['shirt'],
    3: ['map', 'medicine'],
    4: ['plane', 'tape'],
    5: ['bag', 'computer'],
    6: ['bus', 'creature', 'meat'],
}

# Define the moves
moves = [
    (6, None, 'creature'),      # Remove the creature from Box 6
    (3, None, 'map'),           # Remove the map from Box 3
    (3, None, 'medicine'),      # Remove the medicine from Box 3
    (5, 4, 'computer'),         # Move the computer from Box 5 to Box 4
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