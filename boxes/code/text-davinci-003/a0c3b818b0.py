# Initialize the boxes
boxes = {
    0: ['bowl', 'creature'],
    1: ['drug', 'key', 'shirt'],
    2: [],
    3: ['gift', 'paper'],
    4: [],
    5: ['bag', 'computer', 'letter'],
    6: ['stone'],
}

# Define the moves
moves = [
    (6, 3, 'stone'),        # Move the stone from Box 6 to Box 3
    (0, 6, 'bowl'),         # Move the bowl from Box 0 to Box 6
    (0, 6, 'creature'),     # Move the creature from Box 0 to Box 6
    (None, 6, 'rose'),      # Put the rose into Box 6
    (None, 4, 'fish'),      # Put the fish into Box 4
    (5, 4, 'bag'),          # Move the bag from Box 5 to Box 4
    (5, 4, 'letter'),       # Move the letter from Box 5 to Box 4
    (6, None, 'bowl'),      # Remove the bowl from Box 6
    (6, None, 'creature'),  # Remove the creature from Box 6
    (5, None, 'computer'),  # Remove the computer from Box 5
    (3, 6, 'gift'),         # Move the gift from Box 3 to Box 6
    (3, 6, 'stone'),        # Move the stone from Box 3 to Box 6
    (None, 0, 'bag'),       # Move the bag from Box 4 to Box 0
    (0, None, 'bag'),       # Remove the bag from Box 0
    (3, 2, 'paper'),        # Move the paper from Box 3 to Box 2
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