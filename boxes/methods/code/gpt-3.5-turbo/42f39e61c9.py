# Initialize the boxes
boxes = {
    0: ['cross', 'dish', 'pot'],
    1: [],
    2: [],
    3: ['cigarette'],
    4: ['shoe'],
    5: ['mirror', 'sheet'],
    6: ['chemical', 'seed', 'stone'],
}

# Define the moves
moves = [
    (3, None, 'cigarette'),     # Remove the cigarette from Box 3
    (None, 4, 'apple'),         # Put the apple into Box 4
    (None, 4, 'drink'),         # Put the drink into Box 4
    (4, None, 'apple'),         # Remove the apple from Box 4
    (4, None, 'drink'),         # Remove the drink from Box 4
    (None, 1, 'book'),          # Put the book into Box 1
    (1, 4, 'book'),             # Move the book from Box 1 to Box 4
    (6, None, 'stone'),         # Remove the stone from Box 6
    (0, 1, 'dish'),             # Move the dish from Box 0 to Box 1
    (None, 2, 'game'),          # Put the game into Box 2
    (None, 2, 'magazine'),      # Put the magazine into Box 2
    (1, None, 'dish'),          # Remove the dish from Box 1
    (4, 1, 'book'),             # Move the book from Box 4 to Box 1
    (2, None, 'game'),          # Remove the game from Box 2
    (2, None, 'magazine')       # Remove the magazine from Box 2
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