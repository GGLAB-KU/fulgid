# Initialize the boxes
boxes = {
    0: ['computer'],
    1: ['cheese', 'sheet'],
    2: ['document', 'engine'],
    3: ['camera', 'chemical', 'coffee'],
    4: ['block', 'newspaper'],
    5: ['ball', 'shirt'],
    6: [],
}

# Define the moves
moves = [
    (1, 0, 'cheese'),       # Move the cheese from Box 1 to Box 0
    (None, 0, 'pot'),       # Put the pot into Box 0
    (0, None, 'pot'),       # Remove the pot from Box 0
    (None, 0, 'bottle'),    # Put the bottle into Box 0
    (1, None, 'sheet'),     # Remove the sheet from Box 1
    (0, 1, 'cheese'),       # Move the cheese from Box 0 to Box 1
    (0, 1, 'computer'),     # Move the computer from Box 0 to Box 1
    (None, 4, 'ticket'),    # Put the ticket into Box 4
    (5, None, 'ball'),      # Remove the ball from Box 5
    (4, None, 'block'),     # Remove the block from Box 4
    (4, None, 'ticket'),    # Remove the ticket from Box 4
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