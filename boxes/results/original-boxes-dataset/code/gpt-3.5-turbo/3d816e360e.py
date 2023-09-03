# Initialize the boxes
boxes = {
    0: ['boot', 'chemical', 'shirt'],
    1: ['bomb', 'television'],
    2: ['dress', 'fan', 'phone'],
    3: ['wheel'],
    4: ['coffee'],
    5: ['fig'],
    6: ['ball', 'block', 'cheese'],
}

# Define the moves
moves = [
    (6, None, 'cheese'),           # Remove the cheese from Box 6
    (1, 4, 'bomb'),                # Move the bomb from Box 1 to Box 4
    (1, 4, 'television'),          # Move the television from Box 1 to Box 4
    (6, None, 'block'),            # Remove the block from Box 6
    (4, 1, 'bomb'),                # Move the bomb from Box 4 to Box 1
    (4, 1, 'coffee'),              # Move the coffee from Box 4 to Box 1
    (4, 1, 'television'),          # Move the television from Box 4 to Box 1
    (6, None, 'ball'),             # Remove the ball from Box 6
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