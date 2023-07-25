# Initialize the boxes
boxes = {
    0: ['apple', 'sheet'],
    1: ['tape'],
    2: ['cheese', 'plane'],
    3: ['boot', 'computer', 'disk'],
    4: ['glass', 'machine', 'picture'],
    5: ['bell', 'plant'],
    6: ['ball', 'hat', 'meat'],
}

# Define the moves
moves = [
    (4, 0, 'machine'),   # Move the machine from Box 4 to Box 0
    (3, 5, 'disk'),      # Move the disk from Box 3 to Box 5
    (3, 1, 'computer'),  # Move the computer from Box 3 to Box 1
    (2, 4, 'plane'),     # Move the plane from Box 2 to Box 4
    (3, None, 'boot'),   # Remove the boot from Box 3
    (4, None, 'glass'),  # Remove the glass from Box 4
    (2, 1, 'cheese'),    # Move the cheese from Box 2 to Box 1
    (6, None, 'ball'),   # Remove the ball from Box 6
    (6, None, 'meat')    # Remove the meat from Box 6
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