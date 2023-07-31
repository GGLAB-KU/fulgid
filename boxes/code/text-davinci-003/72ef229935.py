# Initialize the boxes
boxes = {
    0: ['chemical', 'plate'],
    1: ['ball'],
    2: ['brick', 'document', 'engine'],
    3: ['milk', 'train'],
    4: ['cake', 'newspaper'],
    5: ['rose'],
    6: ['fan', 'map', 'shell'],
}

# Define the moves
moves = [
    (None, 0, 'card'),       # Put the card into Box 0
    (5, 1, 'rose'),          # Move the rose from Box 5 to Box 1
    (0, None, 'chemical'),   # Remove the chemical from Box 0
    (0, None, 'plate'),      # Remove the plate from Box 0
    (6, 4, 'map'),           # Move the map from Box 6 to Box 4
    (1, None, 'ball'),       # Remove the ball from Box 1
    (1, None, 'rose'),       # Remove the rose from Box 1
    (None, 6, 'egg'),        # Put the egg into Box 6
    (0, None, 'card'),       # Remove the card from Box 0
    (4, None, 'cake'),       # Remove the cake from Box 4
    (4, None, 'map'),        # Remove the map from Box 4
    (2, None, 'engine'),     # Remove the engine from Box 2
    (None, 3, 'magazine'),   # Put the magazine into Box 3
    (6, None, 'fan'),        # Remove the fan from Box 6
    (3, 5, 'milk'),          # Move the milk from Box 3 to Box 5
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