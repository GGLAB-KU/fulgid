# Initialize the boxes
boxes = {
    0: ['apple', 'paper', 'rock'],
    1: ['block', 'plate', 'wire'],
    2: ['bus', 'note', 'shirt'],
    3: ['boot', 'meat'],
    4: ['map'],
    5: ['bill', 'card', 'flower'],
    6: ['mirror', 'ticket', 'watch'],
}

# Define the moves
moves = [
    (1, None, 'block'),   # Remove the block from Box 1
    (1, None, 'wire'),    # Remove the wire from Box 1
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