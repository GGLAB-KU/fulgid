# Initialize the boxes
boxes = {
    0: ['creature', 'tissue'],
    1: ['fish'],
    2: ['drink', 'radio'],
    3: ['bag', 'cup', 'plant'],
    4: ['map', 'painting', 'tape'],
    5: ['glass', 'mirror', 'phone'],
    6: ['ball', 'brick', 'jacket'],
}

# Define the moves
moves = [
    (3, None, 'bag'),       # Remove the bag from Box 3
    (3, None, 'cup'),       # Remove the cup from Box 3
    (6, None, 'brick'),     # Remove the brick from Box 6
    (6, None, 'jacket'),    # Remove the jacket from Box 6
    (1, 2, 'fish'),         # Move the fish from Box 1 to Box 2
    (4, None, 'painting'),  # Remove the painting from Box 4
    (4, None, 'tape'),      # Remove the tape from Box 4
    (None, 0, 'shirt'),     # Put the shirt into Box 0
    (3, None, 'plant'),     # Remove the plant from Box 3
    (None, 1, 'bill'),      # Put the bill into Box 1
    (5, 6, 'mirror'),       # Move the mirror from Box 5 to Box 6
    (6, None, 'ball'),      # Remove the ball from Box 6
    (6, None, 'mirror')     # Remove the mirror from Box 6
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