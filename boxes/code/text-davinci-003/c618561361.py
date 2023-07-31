# Initialize the boxes
boxes = {
    0: ['apple', 'sheet'],
    1: ['cream', 'pot'],
    2: ['bag', 'cross', 'pipe'],
    3: ['bus', 'meat', 'paper'],
    4: ['bill'],
    5: ['beer', 'bomb'],
    6: ['bottle', 'crown', 'shell'],
}

# Define the moves
moves = [
    (5, 0, 'bomb'),         # Move the bomb from Box 5 to Box 0
    (3, 4, 'meat'),         # Move the meat from Box 3 to Box 4
    (3, 4, 'paper'),        # Move the paper from Box 3 to Box 4
    (1, None, 'cream'),     # Remove the cream from Box 1
    (1, None, 'pot'),       # Remove the pot from Box 1
    (3, 1, 'bus'),          # Move the bus from Box 3 to Box 1
    (5, None, 'beer'),      # Remove the beer from Box 5
    (0, None, 'sheet'),     # Remove the sheet from Box 0
    (2, 1, 'cross'),        # Move the cross from Box 2 to Box 1
    (2, None, 'bag'),       # Remove the bag from Box 2
    (2, None, 'pipe'),      # Remove the pipe from Box 2
    (6, 2, 'crown'),        # Move the crown from Box 6 to Box 2
    (6, 2, 'bottle'),       # Move the bottle from Box 6 to Box 2
    (None, 2, 'game'),      # Put the game into Box 2
    (1, None, 'bus')        # Remove the bus from Box 1
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