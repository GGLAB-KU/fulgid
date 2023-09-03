# Initialize the boxes
boxes = {
    0: ['ball'],
    1: ['apple', 'plane', 'ticket'],
    2: ['tea'],
    3: ['coffee', 'plate', 'string'],
    4: ['leaf'],
    5: ['fish', 'tie', 'train'],
    6: [],
}

# Define the moves
moves = [
    (5, None, 'fish'),       # Remove the fish from Box 5
    (5, None, 'tie'),        # Remove the tie from Box 5
    (5, None, 'train'),      # Remove the train from Box 5
    (None, 2, 'phone'),      # Put the phone into Box 2
    (0, 6, 'ball'),          # Move the ball from Box 0 to Box 6
    (6, 0, 'ball'),          # Move the ball from Box 6 to Box 0
    (0, None, 'ball'),       # Remove the ball from Box 0
    (2, 5, 'tea'),           # Move the tea from Box 2 to Box 5
    (1, 5, 'plane'),         # Move the plane from Box 1 to Box 5
    (None, 0, 'game'),       # Put the game into Box 0
    (None, 4, 'magazine'),   # Put the magazine into Box 4
    (3, 5, 'string'),        # Move the string from Box 3 to Box 5
    (2, None, 'phone'),      # Remove the phone from Box 2
    (0, 1, 'game'),          # Move the game from Box 0 to Box 1
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