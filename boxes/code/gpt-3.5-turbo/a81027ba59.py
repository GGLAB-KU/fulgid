# Initialize the boxes
boxes = {
    0: ['bag', 'cigarette', 'shell'],
    1: ['rock', 'sheet'],
    2: ['painting'],
    3: ['branch'],
    4: [],
    5: ['seed'],
    6: [],
}

# Define the moves
moves = [
    (2, None, 'painting'),      # Remove the painting from Box 2
    (3, None, 'branch'),        # Remove the branch from Box 3
    (0, 5, 'bag'),              # Move the bag from Box 0 to Box 5
    (None, 4, 'game'),          # Put the game into Box 4
    (0, 1, 'cigarette'),        # Move the cigarette from Box 0 to Box 1
    (1, 3, 'rock'),             # Move the rock from Box 1 to Box 3
    (3, None, 'rock'),          # Remove the rock from Box 3
    (1, None, 'cigarette'),     # Remove the cigarette from Box 1
    (1, None, 'sheet')          # Remove the sheet from Box 1
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