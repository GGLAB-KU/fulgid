# Initialize the boxes
boxes = {
    0: ['cross', 'key', 'machine'],
    1: [],
    2: ['bottle'],
    3: ['game'],
    4: ['brain'],
    5: [],
    6: ['beer', 'dish', 'pot'],
}

# Define the moves
moves = [
    (6, None, 'beer'),      # Remove the beer from Box 6
    (6, None, 'dish'),      # Remove the dish from Box 6
    (6, None, 'pot'),       # Remove the pot from Box 6
    (None, 2, 'plant'),     # Put the plant into Box 2
    (4, 2, 'brain'),        # Move the brain from Box 4 to Box 2
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