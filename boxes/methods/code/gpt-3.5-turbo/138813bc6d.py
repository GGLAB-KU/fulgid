# Initialize the boxes
boxes = {
    0: ['note'],
    1: ['leaf', 'map'],
    2: [],
    3: ['bell', 'computer', 'suit'],
    4: ['cake', 'ring', 'rose'],
    5: ['cigarette', 'cross'],
    6: ['ball', 'machine', 'television'],
}

# Define the moves
moves = [
    (3, None, 'bell'),    # Remove the bell from Box 3
    (None, 1, 'phone'),   # Put the phone into Box 1
    (0, None, 'note')     # Remove the note from Box 0
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