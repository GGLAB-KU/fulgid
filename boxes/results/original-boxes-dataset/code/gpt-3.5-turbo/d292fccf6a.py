# Initialize the boxes
boxes = {
    0: [],
    1: ['bowl', 'gift', 'rose'],
    2: ['jacket'],
    3: ['glass', 'rock'],
    4: [],
    5: ['meat'],
    6: [],
}

# Define the moves
moves = [
    (None, 3, 'drug'),   # Put the drug into Box 3
    (5, None, 'meat')    # Remove the meat from Box 5
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