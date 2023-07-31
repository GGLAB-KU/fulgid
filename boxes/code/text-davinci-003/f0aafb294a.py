# Initialize the boxes
boxes = {
    0: ['bread', 'guitar', 'pot'],
    1: ['cream', 'disk'],
    2: ['bag', 'shell'],
    3: ['clock', 'stone'],
    4: ['creature', 'milk'],
    5: ['car', 'cigarette', 'gift'],
    6: ['cross'],
}

# Define the moves
moves = [
    (6, None, 'cross'),       # Remove the cross from Box 6
    (2, None, 'shell'),       # Remove the shell from Box 2
    (1, 2, 'cream'),          # Move the cream from Box 1 to Box 2
    (3, None, 'clock'),       # Remove the clock from Box 3
    (2, None, 'bag'),         # Remove the bag from Box 2
    (0, 3, 'guitar'),         # Move the guitar from Box 0 to Box 3
    (0, 3, 'pot'),            # Move the pot from Box 0 to Box 3
    (None, 2, 'brain'),       # Put the brain into Box 2
    (None, 2, 'computer'),    # Put the computer into Box 2
    (1, None, 'disk'),        # Remove the disk from Box 1
    (2, None, 'computer')     # Remove the computer from Box 2
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