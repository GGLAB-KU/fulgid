# Initialize the boxes
boxes = {
    0: ['boot'],
    1: ['card', 'leaf'],
    2: [],
    3: ['plane'],
    4: ['game', 'phone'],
    5: ['bowl', 'tape', 'tea'],
    6: ['chemical', 'guitar'],
}

# Define the moves
moves = [
    (None, 6, 'drug'),       # Put the drug into Box 6
    (6, 0, 'drug'),          # Move the drug from Box 6 to Box 0
    (5, None, 'bowl'),       # Remove the bowl from Box 5
    (5, None, 'tape'),       # Remove the tape from Box 5
    (5, None, 'tea'),        # Remove the tea from Box 5
    (None, 1, 'bus'),        # Put the bus into Box 1
    (4, None, 'phone'),      # Remove the phone from Box 4
    (1, 2, 'bus'),           # Move the bus from Box 1 to Box 2
    (1, 5, 'leaf'),          # Move the leaf from Box 1 to Box 5
    (4, None, 'game'),       # Remove the game from Box 4
    (2, 4, 'bus'),           # Move the bus from Box 2 to Box 4
    (None, 3, 'television'),  # Put the television into Box 3
    (5, 0, 'leaf'),          # Move the leaf from Box 5 to Box 0
    (None, 5, 'shoe')        # Put the shoe into Box 5
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