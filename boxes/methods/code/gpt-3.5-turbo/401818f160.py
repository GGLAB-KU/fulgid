# Initialize the boxes
boxes = {
    0: ['fish', 'ice'],
    1: [],
    2: ['bread', 'note'],
    3: ['glass'],
    4: [],
    5: ['bomb', 'knife'],
    6: ['disk'],
}

# Define the moves
moves = [
    (5, 1, 'knife'),    # Move the knife from Box 5 to Box 1
    (None, 6, 'cash'),  # Put the cash into Box 6
    (None, 0, 'milk'),  # Put the milk into Box 0
    (1, None, 'knife'), # Remove the knife from Box 1
    (0, None, 'fish'),  # Remove the fish from Box 0
    (6, None, 'disk'),  # Remove the disk from Box 6
    (None, 6, 'tea'),   # Put the tea into Box 6
    (2, 3, 'bread'),    # Move the bread from Box 2 to Box 3
    (5, 1, 'bomb'),     # Move the bomb from Box 5 to Box 1
    (6, None, 'cash'),  # Remove the cash from Box 6
    (None, 2, 'apple')  # Put the apple into Box 2
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