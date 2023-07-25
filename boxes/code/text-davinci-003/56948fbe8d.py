# Initialize the boxes
boxes = {
    0: ['crown', 'game', 'hat'],
    1: ['boat'],
    2: [],
    3: [],
    4: ['cream', 'disk', 'phone'],
    5: ['bag', 'bill', 'sheet'],
    6: ['flower', 'shell'],
}

# Define the moves
moves = [
    (0, None, 'crown'),     # Remove the crown from Box 0
    (6, 2, 'flower'),       # Move the flower from Box 6 to Box 2
    (6, 2, 'shell'),        # Move the shell from Box 6 to Box 2
    (0, 6, 'game'),         # Move the game from Box 0 to Box 6
    (0, 6, 'hat'),          # Move the hat from Box 0 to Box 6
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