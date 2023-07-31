# Initialize the boxes
boxes = {
    0: ['cross'],
    1: ['wheel'],
    2: [],
    3: ['fig', 'rock', 'shirt'],
    4: [],
    5: ['computer', 'letter', 'medicine'],
    6: ['leaf', 'phone', 'tea'],
}

# Define the moves
moves = [
    (None, 1, 'cigarette'),     # Put the cigarette into Box 1
    (None, 1, 'pipe'),          # Put the pipe into Box 1
    (None, 0, 'television'),    # Put the television into Box 0
    (0, None, 'television'),    # Remove the television from Box 0
    (5, None, 'computer'),      # Remove the computer from Box 5
    (5, None, 'letter'),        # Remove the letter from Box 5
    (5, None, 'medicine'),      # Remove the medicine from Box 5
    (1, 5, 'cigarette'),        # Move the cigarette from Box 1 to Box 5
    (1, 5, 'wheel'),            # Move the wheel from Box 1 to Box 5
    (None, 0, 'card'),          # Put the card into Box 0
    (None, 0, 'egg'),           # Put the egg into Box 0
    (0, None, 'cross'),         # Remove the cross from Box 0
    (None, 4, 'bag'),           # Put the bag into Box 4
    (0, None, 'card'),          # Remove the card from Box 0
    (0, 4, 'egg'),              # Move the egg from Box 0 to Box 4
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