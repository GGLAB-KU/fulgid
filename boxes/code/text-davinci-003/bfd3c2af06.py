# Initialize the boxes
boxes = {
    0: ['file'],
    1: ['bell', 'newspaper', 'paper'],
    2: ['document', 'fan'],
    3: ['beer', 'train'],
    4: ['engine', 'flower', 'game'],
    5: [],
    6: ['drink'],
}

# Define the moves
moves = [
    (0, None, 'file'),      # Remove the file from Box 0
    (4, None, 'engine'),    # Remove the engine from Box 4
    (None, 4, 'bread'),     # Put the bread into Box 4
    (4, None, 'bread')      # Remove the bread from Box 4
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