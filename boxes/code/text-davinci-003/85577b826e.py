# Initialize the boxes
boxes = {
    0: [],
    1: ['newspaper', 'shell'],
    2: [],
    3: [],
    4: ['book'],
    5: [],
    6: ['document'],
}

# Define the moves
moves = [
    (None, 5, 'milk'),       # Put the milk into Box 5
    (None, 5, 'plate'),      # Put the plate into Box 5
    (5, None, 'plate'),      # Remove the plate from Box 5
    (5, None, 'milk'),       # Remove the milk from Box 5
    (None, 2, 'ball'),       # Put the ball into Box 2
    (None, 2, 'letter'),     # Put the letter into Box 2
    (2, None, 'ball'),       # Remove the ball from Box 2
    (None, 5, 'bread'),      # Put the bread into Box 5
    (None, 2, 'dish'),       # Put the dish into Box 2
    (6, 3, 'document'),      # Move the document from Box 6 to Box 3
    (None, 2, 'file'),       # Put the file into Box 2
    (3, None, 'document'),   # Remove the document from Box 3
    (1, 0, 'newspaper'),     # Move the newspaper from Box 1 to Box 0
    (2, 0, 'dish'),          # Move the dish from Box 2 to Box 0
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