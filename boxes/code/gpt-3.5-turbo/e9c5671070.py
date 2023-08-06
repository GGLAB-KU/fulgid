# Initialize the boxes
boxes = {
    0: ['camera', 'magazine', 'shirt'],
    1: ['card', 'wheel'],
    2: [],
    3: ['bill', 'crown', 'guitar'],
    4: ['drug', 'shoe'],
    5: ['bread', 'leaf'],
    6: ['bomb', 'file', 'seed'],
}

# Define the moves
moves = [
    (1, None, 'wheel'),   # Remove the wheel from Box 1
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