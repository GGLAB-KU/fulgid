# Initialize the boxes
boxes = {
    0: ['branch', 'disk'],
    1: ['bowl', 'tea'],
    2: ['cross', 'cup', 'mirror'],
    3: ['dish', 'milk', 'plate'],
    4: ['medicine'],
    5: ['beer', 'boat', 'map'],
    6: ['jacket', 'letter', 'tape'],
}

# Define the moves
moves = [
    (3, None, 'milk'),       # Remove the milk from Box 3
    (3, None, 'plate'),      # Remove the plate from Box 3
    (0, 4, 'disk'),          # Move the disk from Box 0 to Box 4
    (5, 1, 'beer'),          # Move the beer from Box 5 to Box 1
    (6, 0, 'jacket'),        # Move the jacket from Box 6 to Box 0
    (6, 0, 'tape'),          # Move the tape from Box 6 to Box 0
    (4, 5, 'disk'),          # Move the disk from Box 4 to Box 5
    (0, 3, 'tape'),          # Move the tape from Box 0 to Box 3
    (2, 4, 'cross'),         # Move the cross from Box 2 to Box 4
    (1, None, 'beer'),       # Remove the beer from Box 1
    (1, None, 'tea'),        # Remove the tea from Box 1
    (0, 2, 'branch'),        # Move the branch from Box 0 to Box 2
    (1, 6, 'bowl'),          # Move the bowl from Box 1 to Box 6
    (0, None, 'jacket'),     # Remove the jacket from Box 0
    (6, None, 'letter')      # Remove the letter from Box 6
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