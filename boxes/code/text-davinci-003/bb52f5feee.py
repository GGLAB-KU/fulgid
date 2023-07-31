# Initialize the boxes
boxes = {
    0: ['meat', 'plate', 'sheet'],
    1: ['brain', 'gift', 'wire'],
    2: ['book'],
    3: ['branch'],
    4: ['cheese', 'dish', 'fig'],
    5: ['card', 'file'],
    6: ['egg'],
}

# Define the moves
moves = [
    (6, 2, 'egg'),         # Move the egg from Box 6 to Box 2
    (1, None, 'brain'),    # Remove the brain from Box 1
    (1, None, 'gift'),     # Remove the gift from Box 1
    (0, 5, 'meat'),        # Move the meat from Box 0 to Box 5
    (None, 0, 'game'),     # Put the game into Box 0
    (0, None, 'plate'),    # Remove the plate from Box 0
    (0, None, 'sheet'),    # Remove the sheet from Box 0
    (5, None, 'card'),     # Remove the card from Box 5
    (5, None, 'meat'),     # Remove the meat from Box 5
    (2, None, 'book'),     # Remove the book from Box 2
    (2, None, 'egg'),      # Remove the egg from Box 2
    (0, None, 'game'),     # Remove the game from Box 0
    (5, None, 'file'),     # Remove the file from Box 5
    (None, 0, 'magazine'), # Put the magazine into Box 0
    (1, None, 'wire'),     # Remove the wire from Box 1
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