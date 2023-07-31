# Initialize the boxes
boxes = {
    0: ['tea'],
    1: ['ice'],
    2: ['dress'],
    3: ['fish', 'gift', 'tape'],
    4: ['shell'],
    5: ['block', 'clock'],
    6: ['train'],
}

# Define the moves
moves = [
    (1, 6, 'ice'),       # Move the ice from Box 1 to Box 6
    (2, 5, 'dress'),     # Move the dress from Box 2 to Box 5
    (5, None, 'clock'),  # Remove the clock from Box 5
    (5, None, 'dress'),  # Remove the dress from Box 5
    (3, 0, 'fish'),      # Move the fish from Box 3 to Box 0
    (3, 0, 'gift'),      # Move the gift from Box 3 to Box 0
    (3, 1, 'tape'),      # Move the tape from Box 3 to Box 1
    (0, 4, 'tea'),       # Move the tea from Box 0 to Box 4
    (None, 2, 'tissue'), # Put the tissue into Box 2
    (6, 5, 'ice'),       # Move the ice from Box 6 to Box 5
    (5, None, 'ice')     # Remove the ice from Box 5
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