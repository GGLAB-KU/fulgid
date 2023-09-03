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
    (1, 5, 'dish'),   # Move the dish from Box 1 to Box 5
    (1, 5, 'paper')   # Move the paper from Box 1 to Box 5
]

# Execute the moves
for move in moves:
    src, dest, item = move

    boxes[src].remove(item)  # Remove item from source box
    boxes[dest].append(item)  # Add item to destination box

# Print the boxes
for box in boxes:
    print(f"Box {box}: {boxes[box]}")