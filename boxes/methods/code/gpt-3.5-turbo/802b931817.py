# Initialize the boxes
boxes = {
    0: ['dress'],
    1: ['drug', 'milk'],
    2: ['newspaper'],
    3: ['fig'],
    4: ['coat', 'letter', 'paper'],
    5: ['drink', 'shoe'],
    6: ['computer', 'fan', 'tea'],
}

# Define the moves
moves = [
    (0, 3, 'dress'),        # Move the dress from Box 0 to Box 3
    (6, 0, 'fan'),          # Move the fan from Box 6 to Box 0
    (6, 0, 'tea'),          # Move the tea from Box 6 to Box 0
    (6, 1, 'computer'),     # Move the computer from Box 6 to Box 1
    (5, 6, 'shoe'),         # Move the shoe from Box 5 to Box 6
    (3, None, 'dress'),     # Remove the dress from Box 3
    (3, None, 'fig'),       # Remove the fig from Box 3
    (None, 3, 'disk'),      # Put the disk into Box 3
    (1, None, 'computer'),  # Remove the computer from Box 1
    (None, 3, 'shirt'),     # Put the shirt into Box 3
    (None, 3, 'bill'),      # Put the bill into Box 3
    (0, None, 'fan'),       # Remove the fan from Box 0
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