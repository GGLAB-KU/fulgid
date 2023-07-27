# Initialize the boxes
boxes = {
    0: ['computer', 'fish', 'sheet'],
    1: [],
    2: ['rose'],
    3: ['dish', 'glass'],
    4: ['egg'],
    5: ['ticket'],
    6: ['boat', 'hat', 'suit'],
}

# Define the moves
moves = [
    (2, None, 'rose'),       # Remove the rose from Box 2
    (5, None, 'ticket'),     # Remove the ticket from Box 5
    (4, 3, 'egg'),           # Move the egg from Box 4 to Box 3
    (3, 4, 'egg'),           # Move the egg from Box 3 to Box 4
    (3, 4, 'glass'),         # Move the glass from Box 3 to Box 4
    (4, None, 'egg'),        # Remove the egg from Box 4
    (4, None, 'glass'),      # Remove the glass from Box 4
    (3, None, 'dish'),       # Remove the dish from Box 3
    (None, 2, 'painting'),   # Put the painting into Box 2
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