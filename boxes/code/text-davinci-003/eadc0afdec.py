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