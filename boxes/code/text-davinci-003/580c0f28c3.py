# Initialize the boxes
boxes = {
    0: ['plane'],
    1: ['apple', 'branch', 'letter'],
    2: [],
    3: ['bell', 'watch'],
    4: ['fan'],
    5: ['crown'],
    6: ['cake', 'gift', 'painting'],
}

# Define the moves
moves = [
    (5, None, 'crown'),       # Remove the crown from Box 5
    (0, 2, 'plane'),          # Move the plane from Box 0 to Box 2
    (3, None, 'bell'),        # Remove the bell from Box 3
    (None, 0, 'meat'),        # Put the meat into Box 0
    (3, 0, 'watch'),          # Move the watch from Box 3 to Box 0
    (2, 0, 'plane'),          # Move the plane from Box 2 to Box 0
    (0, 2, 'plane'),          # Move the plane from Box 0 to Box 2
    (None, 4, 'beer'),        # Put the beer into Box 4
    (None, 4, 'crown'),       # Put the crown into Box 4
    (None, 0, 'plant'),       # Put the plant into Box 0
    (4, None, 'fan'),         # Remove the fan from Box 4
    (4, 5, 'crown'),          # Move the crown from Box 4 to Box 5
    (6, None, 'gift'),        # Remove the gift from Box 6
    (6, None, 'painting')     # Remove the painting from Box 6
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