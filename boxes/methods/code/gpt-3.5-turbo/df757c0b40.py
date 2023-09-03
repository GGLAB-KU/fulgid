# Initialize the boxes
boxes = {
    0: ['block', 'hat', 'leaf'],
    1: ['bottle', 'drug', 'ice'],
    2: ['car', 'ring'],
    3: ['pipe'],
    4: ['document', 'file'],
    5: ['cream', 'wire'],
    6: ['boot'],
}

# Define the moves
moves = [
    (0, 6, 'block'),   # Move the block from Box 0 to Box 6
    (0, 6, 'leaf'),    # Move the leaf from Box 0 to Box 6
    (None, 3, 'clock') # Put the clock into Box 3
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