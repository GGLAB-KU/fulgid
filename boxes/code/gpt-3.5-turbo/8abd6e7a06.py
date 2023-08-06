# Initialize the boxes
boxes = {
    0: ['machine', 'painting'],
    1: ['ball', 'shell'],
    2: [],
    3: ['train'],
    4: ['gift', 'paper', 'wheel'],
    5: ['computer', 'phone', 'rock'],
    6: ['bill', 'cream', 'meat'],
}

# Define the moves
moves = [
    (6, 0, 'meat'),     # Move the meat from Box 6 to Box 0
    (3, None, 'train'), # Remove the train from Box 3
    (4, None, 'gift'),  # Remove the gift from Box 4
    (4, None, 'wheel'), # Remove the wheel from Box 4
    (6, None, 'cream'), # Remove the cream from Box 6
    (0, None, 'machine'),  # Remove the machine from Box 0
    (None, 3, 'fig'),   # Put the fig into Box 3
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