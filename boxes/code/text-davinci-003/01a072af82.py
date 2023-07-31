# Initialize the boxes
boxes = {
    0: ['brick', 'cup', 'plane'],
    1: ['dish', 'paper', 'tie'],
    2: ['gift'],
    3: ['brain'],
    4: ['drug', 'glass'],
    5: ['string'],
    6: ['radio', 'tea'],
}

# Define the moves
moves = [
    (1, 5, 'dish'),     # Move the dish from Box 1 to Box 5
    (1, 5, 'paper'),    # Move the paper from Box 1 to Box 5
    (4, None, 'drug'),  # Remove the drug from Box 4
    (0, None, 'brick'), # Remove the brick from Box 0
    (0, None, 'cup'),   # Remove the cup from Box 0
    (4, None, 'glass'), # Remove the glass from Box 4
    (1, None, 'tie'),   # Remove the tie from Box 1
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