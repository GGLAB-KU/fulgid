# Initialize the boxes
boxes = {
    0: ['coffee', 'rock'],
    1: [],
    2: [],
    3: ['crown', 'picture', 'plane'],
    4: ['television'],
    5: ['glass', 'phone'],
    6: ['creature', 'ticket'],
}

# Define the moves
moves = [
    (None, 1, 'ring'),   # Put the ring into Box 1
    (1, 6, 'ring'),      # Move the ring from Box 1 to Box 6
    (3, None, 'picture') # Remove the picture from Box 3
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