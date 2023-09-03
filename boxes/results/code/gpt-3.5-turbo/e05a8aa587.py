# Initialize the boxes
boxes = {
    0: ['bottle', 'brick', 'train'],
    1: ['clock', 'gift'],
    2: ['camera', 'leaf', 'pipe'],
    3: ['ball'],
    4: ['milk', 'plant'],
    5: ['machine', 'paper'],
    6: ['hat', 'key', 'shell'],
}

# Define the moves
moves = [
    (3, 4, 'ball'),         # Move the ball from Box 3 to Box 4
    (2, 1, 'pipe'),         # Move the pipe from Box 2 to Box 1
    (4, 3, 'ball'),         # Move the ball from Box 4 to Box 3
    (4, None, 'computer'),  # Put the computer into Box 4
    (3, None, 'ball'),      # Remove the ball from Box 3
    (3, None, 'milk'),      # Remove the milk from Box 3
    (6, 2, 'key'),          # Move the key from Box 6 to Box 2
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