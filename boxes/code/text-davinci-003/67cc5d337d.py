# Initialize the boxes
boxes = {
    0: ['bill', 'magazine', 'tape'],
    1: ['cup', 'flower'],
    2: [],
    3: ['glass'],
    4: ['cigarette'],
    5: ['chemical', 'key'],
    6: ['hat', 'meat'],
}

# Define the moves
moves = [
    (0, None, 'bill'),       # Remove the bill from Box 0
    (0, None, 'tape'),       # Remove the tape from Box 0
    (0, None, 'magazine'),   # Remove the magazine from Box 0
    (6, 0, 'hat'),           # Move the hat from Box 6 to Box 0
    (None, 0, 'plate'),      # Put the plate into Box 0
    (None, 6, 'computer'),   # Put the computer into Box 6
    (None, 6, 'creature')    # Put the creature into Box 6
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