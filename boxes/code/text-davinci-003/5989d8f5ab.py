# Initialize the boxes
boxes = {
    0: [],
    1: ['cheese', 'drug', 'gift'],
    2: [],
    3: ['radio', 'wheel'],
    4: ['apple', 'dish'],
    5: ['clock', 'cup', 'leaf'],
    6: ['bus', 'cross'],
}

# Define the moves
moves = [
    (None, 4, 'brick'),       # Put the brick into Box 4
    (6, 3, 'cross'),          # Move the cross from Box 6 to Box 3
    (3, None, 'cross'),       # Remove the cross from Box 3
    (3, None, 'radio'),       # Remove the radio from Box 3
    (1, None, 'drug'),        # Remove the drug from Box 1
    (5, None, 'clock'),       # Remove the clock from Box 5
    (None, 1, 'television')    # Put the television into Box 1
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