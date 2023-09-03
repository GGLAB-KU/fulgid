# Initialize the boxes
boxes = {
    0: ['bone', 'dress', 'newspaper'],
    1: ['ring', 'rose'],
    2: ['brain', 'drug', 'fig'],
    3: [],
    4: ['medicine'],
    5: ['cheese', 'creature', 'tape'],
    6: ['branch', 'crown', 'glass'],
}

# Define the moves
moves = [
    (2, None, 'fig'),    # Remove the fig from Box 2
    (None, 1, 'drink')    # Put the drink into Box 1
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