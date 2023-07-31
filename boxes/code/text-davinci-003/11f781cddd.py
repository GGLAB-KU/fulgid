# Initialize the boxes
boxes = {
    0: ['tie'],
    1: ['bus', 'cream'],
    2: ['ball', 'bill'],
    3: ['bomb', 'car'],
    4: ['brick', 'sheet', 'wire'],
    5: ['knife', 'phone', 'train'],
    6: [],
}

# Define the moves
moves = [
    (4, None, 'sheet'),     # Remove the sheet from Box 4
    (4, None, 'wire'),      # Remove the wire from Box 4
    (1, 0, 'bus'),          # Move the bus from Box 1 to Box 0
    (1, 0, 'cream'),        # Move the cream from Box 1 to Box 0
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