# Initialize the boxes
boxes = {
    0: ['cream', 'phone'],
    1: [],
    2: ['cross', 'gift', 'plate'],
    3: ['ball', 'document'],
    4: ['bag', 'jacket', 'rose'],
    5: ['ice', 'knife'],
    6: ['egg'],
}

# Define the moves
moves = [
    (6, 0, 'egg'),          # Move the egg from Box 6 to Box 0
    (5, 6, 'knife'),        # Move the knife from Box 5 to Box 6
    (4, None, 'rose'),      # Remove the rose from Box 4
    (2, None, 'cross'),     # Remove the cross from Box 2
    (2, None, 'gift'),      # Remove the gift from Box 2
    (2, None, 'plate'),     # Remove the plate from Box 2
    (5, 4, 'ice'),          # Move the ice from Box 5 to Box 4
    (6, None, 'knife'),     # Remove the knife from Box 6
    (4, 1, 'ice'),          # Move the ice from Box 4 to Box 1
    (0, 2, 'cream'),        # Move the cream from Box 0 to Box 2
    (0, 2, 'phone'),        # Move the phone from Box 0 to Box 2
    (4, 0, 'bag'),          # Move the bag from Box 4 to Box 0
    (4, 0, 'jacket'),       # Move the jacket from Box 4 to Box 0
    (None, 4, 'wheel'),     # Put the wheel into Box 4
    (None, 1, 'brick'),     # Put the brick into Box 1
    (3, 4, 'document'),     # Move the document from Box 3 to Box 4
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