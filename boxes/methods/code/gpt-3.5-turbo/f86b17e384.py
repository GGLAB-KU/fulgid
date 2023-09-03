# Initialize the boxes
boxes = {
    0: [],
    1: ['card', 'cigarette', 'painting'],
    2: ['cup', 'knife'],
    3: ['hat', 'mirror'],
    4: [],
    5: ['dish', 'gift', 'watch'],
    6: ['cheese'],
}

# Define the moves
moves = [
    (1, None, 'card'),       # Remove the card from Box 1
    (5, 6, 'dish'),          # Move the dish from Box 5 to Box 6
    (5, 6, 'watch'),         # Move the watch from Box 5 to Box 6
    (3, None, 'mirror'),     # Remove the mirror from Box 3
    (1, None, 'cigarette'),  # Remove the cigarette from Box 1
    (5, None, 'gift'),       # Remove the gift from Box 5
    (3, None, 'hat'),        # Remove the hat from Box 3
    (None, 1, 'string'),     # Put the string into Box 1
    (6, 1, 'cheese'),        # Move the cheese from Box 6 to Box 1
    (3, None, 'seed'),       # Put the seed into Box 3
    (3, 6, 'seed'),          # Move the seed from Box 3 to Box 6
    (2, None, 'cup')         # Remove the cup from Box 2
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