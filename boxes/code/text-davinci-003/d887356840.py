# Initialize the boxes
boxes = {
    0: ['ball'],
    1: ['coat', 'drink', 'pot'],
    2: ['drug', 'egg', 'plate'],
    3: ['cup'],
    4: ['car', 'cash', 'newspaper'],
    5: ['apple', 'bus', 'stone'],
    6: ['bone', 'ice', 'medicine'],
}

# Define the moves
moves = [
    (3, None, 'cup'),       # Remove the cup from Box 3
    (6, None, 'bone'),      # Remove the bone from Box 6
    (6, None, 'medicine'),  # Remove the medicine from Box 6
    (4, 0, 'car'),          # Move the car from Box 4 to Box 0
    (2, None, 'plate'),     # Remove the plate from Box 2
    (None, 2, 'bowl'),      # Put the bowl into Box 2
    (4, None, 'cash'),      # Remove the cash from Box 4
    (6, None, 'ice'),       # Remove the ice from Box 6
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