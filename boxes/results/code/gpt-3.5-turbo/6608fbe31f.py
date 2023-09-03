# Initialize the boxes
boxes = {
    0: ['coat', 'cross', 'wire'],
    1: ['shirt'],
    2: ['ticket', 'wheel'],
    3: [],
    4: ['radio'],
    5: ['branch', 'hat', 'phone'],
    6: [],
}

# Define the moves
moves = [
    (5, 2, 'phone'),   # Move the phone from Box 5 to Box 2
    (5, None, 'hat'),  # Remove the hat from Box 5
    (0, None, 'coat'), # Remove the coat from Box 0
    (0, None, 'wire'), # Remove the wire from Box 0
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