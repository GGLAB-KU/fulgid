# Initialize the boxes
boxes = {
    0: ['milk'],
    1: ['disk', 'flower'],
    2: ['coat', 'knife'],
    3: ['bread', 'string'],
    4: ['chemical', 'guitar'],
    5: [],
    6: ['boat'],
}

# Define the moves
moves = [
    (1, None, 'disk'),       # Remove the disk from Box 1
    (0, None, 'milk'),       # Remove the milk from Box 0
    (4, None, 'guitar'),     # Remove the guitar from Box 4
    (4, 0, 'chemical'),      # Move the chemical from Box 4 to Box 0
    (None, 4, 'car'),        # Put the car into Box 4
    (0, None, 'chemical'),   # Remove the chemical from Box 0
    (None, 5, 'document'),   # Put the document into Box 5
    (1, None, 'flower'),     # Remove the flower from Box 1
    (None, 4, 'plate'),      # Put the plate into Box 4
    (None, 4, 'wire'),       # Put the wire into Box 4
    (3, None, 'bread')       # Remove the bread from Box 3
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