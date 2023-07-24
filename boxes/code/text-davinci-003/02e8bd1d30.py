# Initialize the boxes
boxes = {
    0: ['chemical', 'milk'],
    1: ['beer', 'bottle'],
    2: ['camera'],
    3: ['drink'],
    4: ['plant'],
    5: ['machine'],
    6: ['watch'],
}

# Define the moves
moves = [
    (5, 3, 'machine'),   # Move the machine from Box 5 to Box 3
    (None, 5, 'drink'),  # Put the drink into Box 5
    (0, None, 'chemical'),  # Remove the chemical from Box 0
    (0, None, 'milk'),  # Remove the milk from Box 0
    (1, None, 'beer'),  # Remove the beer from Box 1
    (1, None, 'bottle'),  # Remove the bottle from Box 1
    (2, None, 'camera'),  # Remove the camera from Box 2
    (3, None, 'drink'),  # Remove the drink from Box 3
    (4, None, 'plant'),  # Remove the plant from Box 4
    (6, None, 'watch'),  # Remove the watch from Box 6
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