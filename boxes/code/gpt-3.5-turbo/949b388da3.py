# Initialize the boxes
boxes = {
    0: ['radio'],
    1: ['map', 'tea'],
    2: ['file', 'medicine', 'tape'],
    3: ['brick', 'disk', 'wheel'],
    4: ['bomb', 'shell'],
    5: ['bowl', 'plane'],
    6: ['bill', 'fish', 'letter'],
}

# Define the moves
moves = [
    (3, 1, 'brick'),    # Move the brick from Box 3 to Box 1
    (5, None, 'plane'), # Remove the plane from Box 5
    (2, 3, 'medicine'), # Move the medicine from Box 2 to Box 3
    (5, None, 'bowl'),  # Remove the bowl from Box 5
    (2, None, 'tape'),  # Remove the tape from Box 2
    (0, None, 'radio')  # Remove the radio from Box 0
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