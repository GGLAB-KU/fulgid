# Initialize the boxes
boxes = {
    0: ['boat', 'cake', 'magazine'],
    1: ['game'],
    2: ['shoe'],
    3: ['document', 'rose'],
    4: ['cream'],
    5: ['bowl', 'guitar', 'tea'],
    6: ['bone', 'egg'],
}

# Define the moves
moves = [
    (None, 4, 'book'),    # Put the book into Box 4
    (5, None, 'tea'),     # Remove the tea from Box 5
    (3, None, 'document') # Remove the document from Box 3
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