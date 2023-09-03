# Initialize the boxes
boxes = {
    0: ['bowl'],
    1: ['tissue'],
    2: [],
    3: [],
    4: ['chemical', 'leaf', 'plane'],
    5: ['bell', 'glass', 'meat'],
    6: ['fan', 'knife', 'picture'],
}

# Define the moves
moves = [
    (5, None, 'bell'),       # Remove the bell from Box 5
    (5, None, 'glass'),      # Remove the glass from Box 5
    (None, 3, 'bus'),        # Put the bus into Box 3
    (None, 3, 'sheet'),      # Put the sheet into Box 3
    (4, 3, 'chemical'),      # Move the chemical from Box 4 to Box 3
    (None, 5, 'shirt'),      # Put the shirt into Box 5
    (3, None, 'sheet'),      # Remove the sheet from Box 3
    (4, 1, 'leaf'),          # Move the leaf from Box 4 to Box 1
    (4, 1, 'plane'),         # Move the plane from Box 4 to Box 1
    (1, None, 'tissue'),     # Remove the tissue from Box 1
    (None, 0, 'cream'),      # Put the cream into Box 0
    (None, 0, 'jacket'),     # Put the jacket into Box 0
    (6, 2, 'knife'),         # Move the knife from Box 6 to Box 2
    (3, None, 'bus'),        # Remove the bus from Box 3
    (3, None, 'chemical'),   # Remove the chemical from Box 3
    (None, 3, 'drug'),       # Put the drug into Box 3
    (0, 2, 'bowl'),          # Move the bowl from Box 0 to Box 2
    (0, 2, 'cream'),         # Move the cream from Box 0 to Box 2
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