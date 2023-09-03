# Initialize the boxes
boxes = {
    0: [],
    1: ['rock'],
    2: ['cup', 'flower', 'knife'],
    3: ['cake', 'leaf'],
    4: ['cream', 'paper'],
    5: ['coffee'],
    6: [],
}

# Define the moves
moves = [
    (3, None, 'leaf'),       # Remove the leaf from Box 3
    (3, None, 'cake'),       # Remove the cake from Box 3
    (1, None, 'rock'),       # Remove the rock from Box 1
    (2, None, 'flower'),     # Remove the flower from Box 2
    (2, None, 'knife'),      # Remove the knife from Box 2
    (None, 2, 'car'),        # Put the car into Box 2
    (None, 4, 'card'),       # Put the card into Box 4
    (2, None, 'car'),        # Remove the car from Box 2
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