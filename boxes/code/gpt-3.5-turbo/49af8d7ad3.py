# Initialize the boxes
boxes = {
    0: ['boat', 'dish', 'leaf'],
    1: [],
    2: ['bottle', 'newspaper'],
    3: ['block', 'clock', 'wire'],
    4: ['disk'],
    5: ['boot', 'brain', 'bread'],
    6: ['beer', 'suit'],
}

# Define the moves
moves = [
    (5, None, 'boot'),       # Remove the boot from Box 5
    (5, 1, 'brain'),         # Move the brain from Box 5 to Box 1
    (5, 1, 'bread'),         # Move the bread from Box 5 to Box 1
    (0, None, 'boat'),       # Remove the boat from Box 0
    (0, None, 'leaf'),       # Remove the leaf from Box 0
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