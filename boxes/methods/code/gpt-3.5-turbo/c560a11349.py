# Initialize the boxes
boxes = {
    0: ['bomb', 'bus', 'leaf'],
    1: ['pot'],
    2: ['cheese', 'ring'],
    3: ['brain', 'cross'],
    4: ['file', 'flower', 'knife'],
    5: ['boot', 'fish', 'painting'],
    6: ['bag', 'bell', 'bone'],
}

# Define the moves
moves = [
    (None, 1, 'dish'),       # Put the dish into Box 1
    (3, None, 'brain'),      # Remove the brain from Box 3
    (3, None, 'cross'),      # Remove the cross from Box 3
    (4, 3, 'file'),          # Move the file from Box 4 to Box 3
    (4, 3, 'knife'),         # Move the knife from Box 4 to Box 3
    (4, 1, 'flower'),        # Move the flower from Box 4 to Box 1
    (5, None, 'fish'),       # Remove the fish from Box 5
    (5, None, 'painting'),   # Remove the painting from Box 5
    (0, None, 'bomb'),       # Remove the bomb from Box 0
    (0, None, 'bus'),        # Remove the bus from Box 0
    (5, None, 'boot')        # Remove the boot from Box 5
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