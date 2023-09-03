# Initialize the boxes
boxes = {
    0: ['bottle', 'game'],
    1: ['crown', 'document', 'fig'],
    2: [],
    3: ['drug', 'plane'],
    4: ['coffee', 'shirt'],
    5: [],
    6: ['bus', 'fish'],
}

# Define the moves
moves = [
    (6, None, 'bus'),   # Remove the bus from Box 6
    (1, 4, 'crown'),    # Move the crown from Box 1 to Box 4
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