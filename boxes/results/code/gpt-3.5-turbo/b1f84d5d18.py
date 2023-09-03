# Initialize the boxes
boxes = {
    0: ['card', 'cheese', 'seed'],
    1: ['bottle', 'plane'],
    2: ['drink', 'egg', 'key'],
    3: ['ball', 'bread', 'rose'],
    4: ['apple'],
    5: ['creature', 'painting'],
    6: ['bill', 'computer', 'jacket'],
}

# Define the moves
moves = [
    (None, 4, 'drug'),       # Put the drug into Box 4
    (5, None, 'creature'),   # Remove the creature from Box 5
    (1, None, 'plane'),      # Remove the plane from Box 1
    (0, None, 'card'),       # Remove the card from Box 0
    (0, None, 'cheese'),     # Remove the cheese from Box 0
    (2, None, 'drink'),      # Remove the drink from Box 2
    (4, 5, 'drug'),          # Move the drug from Box 4 to Box 5
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