# Initialize the boxes
boxes = {
    0: ['clock', 'tape'],
    1: ['drink', 'note', 'watch'],
    2: ['cross', 'radio', 'train'],
    3: ['book', 'pot'],
    4: ['newspaper'],
    5: ['beer', 'medicine'],
    6: ['ball', 'cheese', 'gift'],
}

# Define the moves
moves = [
    (1, None, 'drink'),     # Remove the drink from Box 1
    (3, None, 'book'),      # Remove the book from Box 3
    (0, None, 'tape'),      # Remove the tape from Box 0
    (None, 3, 'apple'),     # Put the apple into Box 3
    (None, 3, 'fig'),       # Put the fig into Box 3
    (6, None, 'gift'),      # Remove the gift from Box 6
    (2, 6, 'cross'),        # Move the cross from Box 2 to Box 6
    (3, None, 'pot'),       # Remove the pot from Box 3
    (3, 0, 'apple'),        # Move the apple from Box 3 to Box 0
    (3, 0, 'fig')           # Move the fig from Box 3 to Box 0
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