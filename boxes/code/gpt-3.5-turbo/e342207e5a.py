# Initialize the boxes
boxes = {
    0: ['coat', 'flower'],
    1: ['tape', 'wheel'],
    2: ['cup', 'leaf', 'medicine'],
    3: ['chemical', 'gift'],
    4: ['creature', 'dress', 'meat'],
    5: [],
    6: ['key'],
}

# Define the moves
moves = [
    (0, None, 'coat'),       # Remove the coat from Box 0
    (0, None, 'flower'),     # Remove the flower from Box 0
    (1, None, 'tape'),       # Remove the tape from Box 1
    (1, None, 'wheel'),      # Remove the wheel from Box 1
    (2, None, 'cup'),        # Remove the cup from Box 2
    (2, None, 'leaf'),       # Remove the leaf from Box 2
    (2, None, 'medicine'),   # Remove the medicine from Box 2
    (3, None, 'chemical'),   # Remove the chemical from Box 3
    (3, None, 'gift'),       # Remove the gift from Box 3
    (4, None, 'creature'),   # Remove the creature from Box 4
    (4, None, 'dress'),      # Remove the dress from Box 4
    (4, None, 'meat'),       # Remove the meat from Box 4
    (6, 0, 'key'),           # Move the key from Box 6 to Box 0
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