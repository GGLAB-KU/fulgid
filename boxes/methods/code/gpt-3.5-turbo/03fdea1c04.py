# Initialize the boxes
boxes = {
    0: ['drug', 'fish', 'shirt'],
    1: ['mirror', 'television'],
    2: ['machine', 'shoe'],
    3: ['ring'],
    4: ['bus', 'rose', 'watch'],
    5: ['engine'],
    6: ['ice', 'pipe'],
}

# Define the moves
moves = [
    (None, 1, 'crown'),     # Put the crown into Box 1
    (None, 2, 'sheet'),     # Put the sheet into Box 2
    (2, 6, 'shoe'),         # Move the shoe from Box 2 to Box 6
    (3, None, 'ring'),      # Remove the ring from Box 3
    (None, 5, 'beer'),      # Put the beer into Box 5
    (None, 5, 'car'),       # Put the car into Box 5
    (1, None, 'mirror'),    # Remove the mirror from Box 1
    (1, None, 'television'), # Remove the television from Box 1
    (4, 3, 'rose'),         # Move the rose from Box 4 to Box 3
    (4, 3, 'watch'),        # Move the watch from Box 4 to Box 3
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