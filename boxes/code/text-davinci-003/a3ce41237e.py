# Initialize the boxes
boxes = {
    0: ['tape', 'television'],
    1: ['computer'],
    2: ['glass', 'paper', 'seed'],
    3: ['bag', 'branch', 'car'],
    4: ['document'],
    5: ['camera', 'letter', 'painting'],
    6: ['tie'],
}

# Define the moves
moves = [
    (0, 6, 'tape'),         # Move the tape from Box 0 to Box 6
    (0, 6, 'television'),   # Move the television from Box 0 to Box 6
    (6, None, 'tape'),      # Remove the tape from Box 6
    (6, None, 'tie')        # Remove the tie from Box 6
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