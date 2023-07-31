# Initialize the boxes
boxes = {
    0: ['key', 'map', 'watch'],
    1: ['milk', 'picture', 'plate'],
    2: ['card', 'guitar', 'ring'],
    3: ['letter', 'paper'],
    4: ['bomb', 'leaf'],
    5: ['chemical', 'gift', 'magazine'],
    6: ['dress', 'train'],
}

# Define the moves
moves = [
    (0, None, 'key'),       # Remove the key from Box 0
    (0, None, 'map'),       # Remove the map from Box 0
    (0, None, 'watch'),     # Remove the watch from Box 0
    (1, None, 'milk'),      # Remove the milk from Box 1
    (1, None, 'picture'),   # Remove the picture from Box 1
    (1, None, 'plate'),     # Remove the plate from Box 1
    (2, None, 'card'),      # Remove the card from Box 2
    (2, None, 'guitar'),    # Remove the guitar from Box 2
    (2, None, 'ring'),      # Remove the ring from Box 2
    (3, None, 'letter'),    # Remove the letter from Box 3
    (3, None, 'paper'),     # Remove the paper from Box 3
    (4, None, 'bomb'),      # Remove the bomb from Box 4
    (4, None, 'leaf'),      # Remove the leaf from Box 4
    (5, None, 'chemical'),  # Remove the chemical from Box 5
    (5, None, 'gift'),      # Remove the gift from Box 5
    (5, None, 'magazine'),  # Remove the magazine from Box 5
    (6, None, 'dress'),     # Remove the dress from Box 6
    (6, None, 'train'),     # Remove the train from Box 6
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