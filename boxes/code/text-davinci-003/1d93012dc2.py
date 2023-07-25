# Initialize the boxes
boxes = {
    0: ['apple', 'shell'],
    1: ['guitar', 'magazine'],
    2: ['cake'],
    3: [],
    4: ['cup', 'engine', 'rose'],
    5: ['ball', 'branch'],
    6: ['card', 'cash', 'key'],
}

# Define the moves
moves = [
    (6, 2, 'card'),         # Move the card from Box 6 to Box 2
    (6, 2, 'key'),          # Move the key from Box 6 to Box 2
    (None, 0, 'tape'),      # Put the tape into Box 0
    (1, None, 'magazine'),  # Remove the magazine from Box 1
    (0, None, 'apple'),     # Remove the apple from Box 0
    (0, None, 'shell'),     # Remove the shell from Box 0
    (1, 5, 'guitar'),       # Move the guitar from Box 1 to Box 5
    (2, None, 'cake'),      # Remove the cake from Box 2
    (2, None, 'card'),      # Remove the card from Box 2
    (2, 6, 'key'),          # Move the key from Box 2 to Box 6
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