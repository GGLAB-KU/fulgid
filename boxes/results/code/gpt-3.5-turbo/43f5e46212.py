# Initialize the boxes
boxes = {
    0: ['clock', 'watch'],
    1: ['map'],
    2: ['gift', 'guitar'],
    3: ['block', 'milk', 'wire'],
    4: ['boat', 'bottle', 'car'],
    5: ['dish', 'ticket'],
    6: ['bag', 'brick', 'chemical'],
}

# Define the moves
moves = [
    (5, None, 'dish'),       # Remove the dish from Box 5
    (None, 1, 'ball'),       # Put the ball into Box 1
    (None, 1, 'bread'),      # Put the bread into Box 1
    (6, 5, 'brick'),         # Move the brick from Box 6 to Box 5
    (0, None, 'clock'),      # Remove the clock from Box 0
    (1, None, 'ball'),       # Remove the ball from Box 1
    (1, None, 'bread'),      # Remove the bread from Box 1
    (4, None, 'boat'),       # Remove the boat from Box 4
    (4, None, 'car'),        # Remove the car from Box 4
    (5, 2, 'brick'),         # Move the brick from Box 5 to Box 2
    (3, 0, 'block'),         # Move the block from Box 3 to Box 0
    (3, 0, 'milk'),          # Move the milk from Box 3 to Box 0
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