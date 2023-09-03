# Initialize the boxes
boxes = {
    0: ['brick', 'wire'],
    1: ['cigarette', 'jacket'],
    2: ['bell', 'bone'],
    3: ['milk', 'tie', 'wheel'],
    4: ['ball', 'newspaper', 'tape'],
    5: ['bus'],
    6: ['chemical', 'rock', 'suit'],
}

# Define the moves
moves = [
    (5, None, 'bus'),           # Remove the bus from Box 5
    (1, None, 'jacket'),        # Remove the jacket from Box 1
    (4, 5, 'newspaper'),        # Move the newspaper from Box 4 to Box 5
    (4, 5, 'tape'),             # Move the tape from Box 4 to Box 5
    (2, None, 'bell'),          # Remove the bell from Box 2
    (3, None, 'milk'),          # Remove the milk from Box 3
    (3, None, 'wheel'),         # Remove the wheel from Box 3
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