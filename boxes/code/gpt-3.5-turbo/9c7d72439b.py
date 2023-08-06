# Initialize the boxes
boxes = {
    0: ['milk'],
    1: ['clock', 'cross'],
    2: ['game', 'letter'],
    3: ['book', 'cup'],
    4: [],
    5: ['ball'],
    6: ['medicine', 'television'],
}

# Define the moves
moves = [
    (2, 1, 'game'),     # Move the game from Box 2 to Box 1
    (0, 6, 'milk'),     # Move the milk from Box 0 to Box 6
    (3, 2, 'book'),     # Move the book from Box 3 to Box 2
    (5, None, 'ball'),  # Remove the ball from Box 5
    (2, None, 'letter'),# Remove the letter from Box 2
    (None, 2, 'fig'),   # Put the fig into Box 2
    (2, 4, 'book'),     # Move the book from Box 2 to Box 4
    (2, 4, 'fig'),      # Move the fig from Box 2 to Box 4
    (3, None, 'cup'),   # Remove the cup from Box 3
    (None, 5, 'coat')   # Put the coat into Box 5
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