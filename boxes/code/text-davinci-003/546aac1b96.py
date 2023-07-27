# Initialize the boxes
boxes = {
    0: ['coat', 'fan'],
    1: ['jacket', 'paper'],
    2: ['tape'],
    3: ['bowl', 'cross', 'key'],
    4: [],
    5: ['television'],
    6: [],
}

# Define the moves
moves = [
    (None, 6, 'cash'),       # Put the cash into Box 6
    (None, 6, 'medicine'),   # Put the medicine into Box 6
    (1, 5, 'jacket'),        # Move the jacket from Box 1 to Box 5
    (1, 5, 'paper'),         # Move the paper from Box 1 to Box 5
    (6, None, 'medicine'),   # Remove the medicine from Box 6
    (None, 0, 'string'),     # Put the string into Box 0
    (0, None, 'coat'),       # Remove the coat from Box 0
    (0, None, 'string'),     # Remove the string from Box 0
    (2, None, 'rose'),       # Put the rose into Box 2
    (2, 6, 'rose'),          # Move the rose from Box 2 to Box 6
    (6, 2, 'cash'),          # Move the cash from Box 6 to Box 2
    (6, None, 'rose'),       # Remove the rose from Box 6
    (5, None, 'television'), # Remove the television from Box 5
    (3, None, 'cross'),      # Remove the cross from Box 3
    (5, None, 'paper')       # Remove the paper from Box 5
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