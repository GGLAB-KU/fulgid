# Initialize the boxes
boxes = {
    0: ['cheese', 'fish', 'radio'],
    1: ['bone', 'bread', 'pot'],
    2: ['bell'],
    3: ['cross'],
    4: ['clock'],
    5: ['disk', 'meat'],
    6: ['book', 'train'],
}

# Define the moves
moves = [
    (6, None, 'book'),       # Remove the book from Box 6
    (2, 4, 'bell'),          # Move the bell from Box 2 to Box 4
    (5, None, 'disk'),       # Remove the disk from Box 5
    (None, 2, 'game'),       # Put the game into Box 2
    (0, 5, 'radio'),         # Move the radio from Box 0 to Box 5
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