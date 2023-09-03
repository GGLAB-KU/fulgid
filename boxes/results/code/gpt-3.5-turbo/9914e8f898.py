# Initialize the boxes
boxes = {
    0: ['card', 'hat'],
    1: ['fish'],
    2: ['bomb'],
    3: ['branch', 'car', 'mirror'],
    4: [],
    5: ['creature', 'watch'],
    6: ['flower', 'ice', 'shoe'],
}

# Define the moves
moves = [
    (6, 4, 'ice'),         # Move the ice from Box 6 to Box 4
    (6, 4, 'shoe'),        # Move the shoe from Box 6 to Box 4
    (1, None, 'fish'),     # Remove the fish from Box 1
    (4, 6, 'shoe'),        # Move the shoe from Box 4 to Box 6
    (2, None, 'bomb'),     # Remove the bomb from Box 2
    (0, None, 'card'),     # Remove the card from Box 0
    (6, 2, 'flower'),      # Move the flower from Box 6 to Box 2
    (6, 2, 'shoe'),        # Move the shoe from Box 6 to Box 2
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