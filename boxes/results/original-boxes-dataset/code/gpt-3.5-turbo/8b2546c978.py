# Initialize the boxes
boxes = {
    0: [],
    1: ['document', 'fan', 'fig'],
    2: ['clock', 'magazine', 'newspaper'],
    3: ['apple', 'cash', 'tape'],
    4: ['bag', 'knife', 'plane'],
    5: ['branch', 'ring'],
    6: ['cup'],
}

# Define the moves
moves = [
    (5, 0, 'branch'),       # Move the branch from Box 5 to Box 0
    (5, 0, 'ring'),         # Move the ring from Box 5 to Box 0
    (2, None, 'clock'),     # Remove the clock from Box 2
    (2, None, 'newspaper'), # Remove the newspaper from Box 2
    (None, 6, 'cross'),     # Put the cross into Box 6
    (2, None, 'magazine'),  # Remove the magazine from Box 2
    (None, 6, 'rose'),      # Put the rose into Box 6
    (6, None, 'cross'),     # Remove the cross from Box 6
    (6, None, 'cup'),       # Remove the cup from Box 6
    (6, None, 'rose'),      # Remove the rose from Box 6
    (0, 5, 'ring'),         # Move the ring from Box 0 to Box 5
    (None, 2, 'meat'),      # Put the meat into Box 2
    (4, None, 'bag'),       # Remove the bag from Box 4
    (4, None, 'knife'),     # Remove the knife from Box 4
    (4, None, 'plane'),     # Remove the plane from Box 4
    (3, None, 'apple'),     # Remove the apple from Box 3
    (3, None, 'cash'),      # Remove the cash from Box 3
    (3, None, 'tape'),      # Remove the tape from Box 3
    (None, 4, 'plane')      # Put the plane into Box 4
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