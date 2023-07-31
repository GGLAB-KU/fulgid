# Initialize the boxes
boxes = {
    0: ['boot', 'bread'],
    1: ['block', 'clock', 'fan'],
    2: ['plant'],
    3: ['book', 'cheese', 'ring'],
    4: ['shoe'],
    5: [],
    6: ['cross', 'gift', 'key'],
}

# Define the moves
moves = [
    (0, None, 'boot'),       # Remove the boot from Box 0
    (6, 0, 'cross'),         # Move the cross from Box 6 to Box 0
    (6, 0, 'key'),           # Move the key from Box 6 to Box 0
    (0, None, 'bread'),      # Remove the bread from Box 0
    (4, 5, 'shoe'),          # Move the shoe from Box 4 to Box 5
    (2, 0, 'plant'),         # Move the plant from Box 2 to Box 0
    (1, None, 'fan'),        # Remove the fan from Box 1
    (None, 5, 'tea'),        # Put the tea into Box 5
    (1, 2, 'clock'),         # Move the clock from Box 1 to Box 2
    (6, 1, 'gift'),          # Move the gift from Box 6 to Box 1
    (1, None, 'block'),      # Remove the block from Box 1
    (1, None, 'gift'),       # Remove the gift from Box 1
    (None, 1, 'apple')       # Put the apple into Box 1
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