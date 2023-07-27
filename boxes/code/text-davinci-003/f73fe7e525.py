# Initialize the boxes
boxes = {
    0: ['block', 'clock', 'computer'],
    1: ['creature', 'fan', 'paper'],
    2: ['guitar', 'wheel'],
    3: ['jacket', 'string', 'television'],
    4: [],
    5: ['bomb'],
    6: ['game'],
}

# Define the moves
moves = [
    (5, 4, 'bomb'),         # Move the bomb from Box 5 to Box 4
    (3, None, 'jacket'),    # Remove the jacket from Box 3
    (4, None, 'bomb'),      # Remove the bomb from Box 4
    (None, 5, 'shoe'),      # Put the shoe into Box 5
    (1, 4, 'fan'),          # Move the fan from Box 1 to Box 4
    (5, None, 'shoe'),      # Remove the shoe from Box 5
    (None, 2, 'apple'),     # Put the apple into Box 2
    (2, None, 'apple'),     # Remove the apple from Box 2
    (2, None, 'guitar'),    # Remove the guitar from Box 2
    (2, None, 'wheel')      # Remove the wheel from Box 2
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