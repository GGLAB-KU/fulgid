# Initialize the boxes
boxes = {
    0: ['bowl'],
    1: ['document', 'fig'],
    2: ['bomb', 'drug', 'shirt'],
    3: ['engine'],
    4: ['block', 'glass', 'suit'],
    5: [],
    6: ['boot', 'cross', 'milk'],
}

# Define the moves
moves = [
    (1, None, 'fig'),     # Remove the fig from Box 1
    (3, None, 'engine'),  # Remove the engine from Box 3
    (1, None, 'document') # Remove the document from Box 1
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