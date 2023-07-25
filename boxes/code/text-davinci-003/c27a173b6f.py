# Initialize the boxes
boxes = {
    0: ['rose'],
    1: [],
    2: ['letter'],
    3: ['game'],
    4: ['bread', 'radio', 'tape'],
    5: ['bell', 'camera', 'clock'],
    6: ['apple', 'computer', 'tie'],
}

# Define the moves
moves = [
    (2, 1, 'letter'),   # Move the letter from Box 2 to Box 1
    (0, None, 'rose'),  # Remove the rose from Box 0
    (None, 0, 'shoe'),  # Put the shoe into Box 0
    (None, 0, 'flower')  # Put the flower into Box 0
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