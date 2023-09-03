# Initialize the boxes
boxes = {
    0: ['beer', 'guitar', 'mirror'],
    1: [],
    2: ['cheese', 'pipe', 'sheet'],
    3: ['coat', 'knife'],
    4: ['cream', 'fan', 'fish'],
    5: [],
    6: ['disk', 'tissue'],
}

# Define the moves
moves = [
    (3, None, 'coat'),      # Remove the coat from Box 3
    (3, None, 'knife'),     # Remove the knife from Box 3
    (4, 6, 'fish'),         # Move the fish from Box 4 to Box 6
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