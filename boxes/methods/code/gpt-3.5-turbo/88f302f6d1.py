# Initialize the boxes
boxes = {
    0: ['bag', 'plant'],
    1: ['car', 'dish', 'game'],
    2: ['rose'],
    3: ['branch', 'stone', 'television'],
    4: ['meat'],
    5: ['dress', 'gift', 'watch'],
    6: ['hat', 'shirt'],
}

# Define the moves
moves = [
    (1, 0, 'dish'),         # Move the dish from Box 1 to Box 0
    (4, 2, 'meat'),         # Move the meat from Box 4 to Box 2
    (3, None, 'television'), # Remove the television from Box 3
    (5, 3, 'gift'),         # Move the gift from Box 5 to Box 3
    (5, 6, 'dress'),        # Move the dress from Box 5 to Box 6
    (3, 5, 'branch'),       # Move the branch from Box 3 to Box 5
    (3, 5, 'gift'),         # Move the gift from Box 3 to Box 5
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