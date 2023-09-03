# Initialize the boxes
boxes = {
    0: ['beer', 'camera', 'rose'],
    1: ['brain'],
    2: ['book', 'coffee', 'tape'],
    3: ['car', 'newspaper'],
    4: ['branch', 'bread'],
    5: ['bill', 'letter'],
    6: ['dress', 'ice', 'tie'],
}

# Define the moves
moves = [
    (5, None, 'letter'),       # Remove the letter from Box 5
    (2, 1, 'coffee'),          # Move the coffee from Box 2 to Box 1
    (2, 1, 'tape'),            # Move the tape from Box 2 to Box 1
    (0, 2, 'camera'),          # Move the camera from Box 0 to Box 2
    (0, 2, 'rose'),            # Move the rose from Box 0 to Box 2
    (0, None, 'beer'),         # Remove the beer from Box 0
    (3, 5, 'car'),             # Move the car from Box 3 to Box 5
    (1, None, 'coffee')        # Remove the coffee from Box 1
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