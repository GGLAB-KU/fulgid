# Initialize the boxes
boxes = {
    0: ['egg'],
    1: ['chemical', 'ring', 'sheet'],
    2: ['document', 'newspaper', 'tissue'],
    3: ['boat', 'dress', 'pipe'],
    4: ['branch', 'guitar', 'letter'],
    5: [],
    6: ['wire'],
}

# Define the moves
moves = [
    (1, None, 'chemical'),     # Remove the chemical from Box 1
    (1, None, 'ring'),         # Remove the ring from Box 1
    (4, 5, 'branch'),           # Move the branch from Box 4 to Box 5
    (6, None, 'wire'),          # Remove the wire from Box 6
    (2, None, 'document'),      # Remove the document from Box 2
    (None, 4, 'shoe'),          # Put the shoe into Box 4
    (4, 0, 'guitar'),           # Move the guitar from Box 4 to Box 0
    (4, None, 'shoe'),          # Remove the shoe from Box 4
    (1, None, 'sheet'),         # Remove the sheet from Box 1
    (None, 0, 'coffee'),        # Put the coffee into Box 0
    (2, None, 'newspaper'),     # Remove the newspaper from Box 2
    (2, None, 'tissue'),        # Remove the tissue from Box 2
    (0, None, 'coffee'),        # Remove the coffee from Box 0
    (0, None, 'egg'),           # Remove the egg from Box 0
    (0, None, 'guitar')         # Remove the guitar from Box 0
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