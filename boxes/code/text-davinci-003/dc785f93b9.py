# Initialize the boxes
boxes = {
    0: ['branch', 'bread'],
    1: ['cream'],
    2: ['boat', 'machine'],
    3: ['document', 'letter', 'phone'],
    4: ['clock', 'drug', 'picture'],
    5: ['card', 'key'],
    6: ['fig', 'ice', 'rose'],
}

# Define the moves
moves = [
    (2, None, 'boat'),       # Remove the boat from Box 2
    (2, None, 'machine'),    # Remove the machine from Box 2
    (3, None, 'document'),   # Remove the document from Box 3
    (3, None, 'letter'),     # Remove the letter from Box 3
    (3, None, 'phone'),      # Remove the phone from Box 3
    (1, None, 'cream'),      # Remove the cream from Box 1
    (4, None, 'picture')     # Remove the picture from Box 4
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