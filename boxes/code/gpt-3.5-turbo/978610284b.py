# Initialize the boxes
boxes = {
    0: [],
    1: ['bomb', 'ice', 'wheel'],
    2: ['picture'],
    3: ['boat', 'cross'],
    4: ['card'],
    5: ['book', 'coat', 'note'],
    6: ['cream', 'egg', 'key'],
}

# Define the moves
moves = [
    (3, None, 'cross'),       # Remove the cross from Box 3
    (2, 3, 'picture'),        # Move the picture from Box 2 to Box 3
    (5, 3, 'book'),           # Move the book from Box 5 to Box 3
    (6, None, 'cream'),       # Remove the cream from Box 6
    (6, None, 'egg'),         # Remove the egg from Box 6
    (6, None, 'key'),         # Remove the key from Box 6
    (3, None, 'boat'),        # Remove the boat from Box 3
    (3, None, 'book'),        # Remove the book from Box 3
    (3, 2, 'picture'),        # Move the picture from Box 3 to Box 2
    (5, 2, 'note'),           # Move the note from Box 5 to Box 2
    (2, None, 'note'),        # Remove the note from Box 2
    (5, 4, 'coat'),           # Move the coat from Box 5 to Box 4
    (None, 3, 'game')         # Put the game into Box 3
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