# Initialize the boxes
boxes = {
    0: ['car'],
    1: ['bone'],
    2: ['chemical', 'cup', 'hat'],
    3: ['clock', 'mirror', 'string'],
    4: ['bell', 'card', 'note'],
    5: [],
    6: ['coffee', 'radio', 'watch'],
}

# Define the moves
moves = [
    (1, None, 'bone'),       # Remove the bone from Box 1
    (6, 0, 'coffee'),        # Move the coffee from Box 6 to Box 0
    (None, 0, 'game'),       # Put the game into Box 0
    (0, None, 'car'),        # Remove the car from Box 0
    (0, None, 'coffee'),     # Remove the coffee from Box 0
    (0, None, 'game'),       # Remove the game from Box 0
    (3, 6, 'mirror'),        # Move the mirror from Box 3 to Box 6
    (3, None, 'clock'),      # Remove the clock from Box 3
    (2, None, 'chemical'),   # Remove the chemical from Box 2
    (3, None, 'string'),     # Remove the string from Box 3
    (6, 1, 'radio'),         # Move the radio from Box 6 to Box 1
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