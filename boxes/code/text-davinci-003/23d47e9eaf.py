# Initialize the boxes
boxes = {
    0: [],
    1: ['coat'],
    2: ['cheese'],
    3: [],
    4: ['knife', 'mirror', 'plate'],
    5: ['painting'],
    6: ['block', 'rose'],
}

# Define the moves
moves = [
    (1, None, 'coat'),       # Remove the coat from Box 1
    (4, None, 'knife'),      # Remove the knife from Box 4
    (4, None, 'mirror'),     # Remove the mirror from Box 4
    (4, None, 'plate'),      # Remove the plate from Box 4
    (5, 3, 'painting'),      # Move the painting from Box 5 to Box 3
    (0, None, 'guitar'),     # Put the guitar into Box 0
    (0, None, 'jacket'),     # Put the jacket into Box 0
    (0, None, 'letter'),     # Put the letter into Box 0
    (0, 1, 'letter'),        # Move the letter from Box 0 to Box 1
    (6, 5, 'rose'),          # Move the rose from Box 6 to Box 5
    (1, None, 'letter'),     # Remove the letter from Box 1
    (6, 2, 'block'),         # Move the block from Box 6 to Box 2
    (0, None, 'cup'),        # Put the cup into Box 0
    (5, None, 'rose'),       # Remove the rose from Box 5
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