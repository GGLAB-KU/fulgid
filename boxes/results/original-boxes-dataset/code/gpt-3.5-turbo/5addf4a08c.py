# Initialize the boxes
boxes = {
    0: ['coat', 'medicine'],
    1: ['apple', 'guitar', 'shell'],
    2: ['bag', 'drink', 'tie'],
    3: ['machine', 'paper', 'watch'],
    4: ['camera', 'seed'],
    5: ['clock'],
    6: ['computer', 'note', 'plant'],
}

# Define the moves
moves = [
    (2, 0, 'tie'),       # Move the tie from Box 2 to Box 0
    (5, 4, 'clock'),     # Move the clock from Box 5 to Box 4
    (2, None, 'bag'),    # Remove the bag from Box 2
    (0, None, 'tie'),    # Remove the tie from Box 0
    (3, 0, 'paper'),     # Move the paper from Box 3 to Box 0
    (0, None, 'coat'),   # Remove the coat from Box 0
    (6, None, 'plant')   # Remove the plant from Box 6
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