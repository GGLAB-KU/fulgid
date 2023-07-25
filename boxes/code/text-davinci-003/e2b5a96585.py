# Initialize the boxes
boxes = {
    0: ['jacket'],
    1: ['machine', 'note'],
    2: [],
    3: ['dress', 'television'],
    4: ['apple', 'bread'],
    5: [],
    6: ['book', 'paper'],
}

# Define the moves
moves = [
    (3, 5, 'television'),   # Move the television from Box 3 to Box 5
    (3, None, 'dress'),     # Remove the dress from Box 3
    (5, None, 'television'), # Remove the television from Box 5
    (6, 1, 'book'),         # Move the book from Box 6 to Box 1
    (0, None, 'jacket'),    # Remove the jacket from Box 0
    (6, None, 'boot'),      # Put the boot into Box 6
    (6, 2, 'boot'),         # Move the boot from Box 6 to Box 2
    (None, 0, 'bottle'),    # Put the bottle into Box 0
    (0, 6, 'bottle'),       # Move the bottle from Box 0 to Box 6
    (None, 5, 'knife'),     # Put the knife into Box 5
    (6, None, 'bottle'),    # Remove the bottle from Box 6
    (6, None, 'paper')      # Remove the paper from Box 6
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