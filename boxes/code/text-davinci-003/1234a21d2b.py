# Initialize the boxes
boxes = {
    0: [],
    1: ['bowl', 'painting'],
    2: ['wire'],
    3: ['chemical', 'ring'],
    4: ['fan', 'flower'],
    5: ['cash'],
    6: ['guitar', 'television'],
}

# Define the moves
moves = [
    (3, None, 'ring'),       # Remove the ring from Box 3
    (1, None, 'painting'),   # Remove the painting from Box 1
    (5, None, 'cash'),       # Remove the cash from Box 5
    (1, None, 'bowl'),       # Remove the bowl from Box 1
    (None, 6, 'phone')       # Put the phone into Box 6
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