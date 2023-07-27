# Initialize the boxes
boxes = {
    0: ['bowl', 'bread', 'suit'],
    1: ['medicine'],
    2: ['ball', 'egg'],
    3: [],
    4: ['fish'],
    5: ['glass', 'tie'],
    6: [],
}

# Define the moves
moves = [
    (1, 4, 'medicine'),   # Move the medicine from Box 1 to Box 4
    (0, None, 'bowl'),    # Remove the bowl from Box 0
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