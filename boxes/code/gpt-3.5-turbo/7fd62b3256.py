# Initialize the boxes
boxes = {
    0: ['chemical', 'leaf', 'shirt'],
    1: ['coffee'],
    2: ['ball', 'beer', 'hat'],
    3: ['bill', 'branch', 'wire'],
    4: ['cream', 'document', 'tissue'],
    5: ['bone', 'rock', 'rose'],
    6: ['bottle', 'brain', 'coat'],
}

# Define the moves
moves = [
    (1, None, 'coffee'),       # Remove the coffee from Box 1
    (3, 1, 'wire'),             # Move the wire from Box 3 to Box 1
    (4, None, 'cream'),         # Remove the cream from Box 4
    (None, 1, 'train'),         # Put the train into Box 1
    (0, None, 'chemical'),      # Remove the chemical from Box 0
    (0, None, 'leaf'),          # Remove the leaf from Box 0
    (0, None, 'shirt'),         # Remove the shirt from Box 0
    (4, 1, 'document'),         # Move the document from Box 4 to Box 1
    (None, 4, 'brick'),         # Put the brick into Box 4
    (3, None, 'bill'),          # Remove the bill from Box 3
    (3, None, 'branch'),        # Remove the branch from Box 3
    (2, 0, 'beer'),             # Move the beer from Box 2 to Box 0
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