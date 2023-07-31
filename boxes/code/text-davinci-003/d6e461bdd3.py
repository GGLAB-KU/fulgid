# Initialize the boxes
boxes = {
    0: [],
    1: ['boat', 'cream'],
    2: ['car', 'gift'],
    3: ['bomb', 'branch', 'stone'],
    4: ['dish'],
    5: ['egg'],
    6: ['plant'],
}

# Define the moves
moves = [
    (6, None, 'plant'),     # Remove the plant from Box 6
    (1, 6, 'cream'),        # Move the cream from Box 1 to Box 6
    (5, 1, 'egg'),          # Move the egg from Box 5 to Box 1
    (6, 1, 'cream'),        # Move the cream from Box 6 to Box 1
    (2, None, 'car'),       # Remove the car from Box 2
    (1, 6, 'boat'),         # Move the boat from Box 1 to Box 6
    (1, 6, 'egg'),          # Move the egg from Box 1 to Box 6
    (3, 4, 'bomb'),         # Move the bomb from Box 3 to Box 4
    (2, 4, 'gift'),         # Move the gift from Box 2 to Box 4
    (4, None, 'dish'),      # Remove the dish from Box 4
    (4, None, 'gift'),      # Remove the gift from Box 4
    (None, 3, 'radio'),     # Put the radio into Box 3
    (1, 5, 'cream')         # Move the cream from Box 1 to Box 5
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