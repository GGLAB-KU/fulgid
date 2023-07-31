# Initialize the boxes
boxes = {
    0: ['bomb', 'card', 'fig'],
    1: ['cigarette', 'map', 'shoe'],
    2: [],
    3: ['bill', 'creature'],
    4: [],
    5: ['magazine'],
    6: [],
}

# Define the moves
moves = [
    (1, 4, 'map'),       # Move the map from Box 1 to Box 4
    (5, None, 'magazine'),   # Remove the magazine from Box 5
    (None, 4, 'plant'),   # Put the plant into Box 4
    (3, None, 'creature')   # Remove the creature from Box 3
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