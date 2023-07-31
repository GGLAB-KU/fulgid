# Initialize the boxes
boxes = {
    0: ['book', 'phone', 'picture'],
    1: ['knife', 'painting'],
    2: ['bottle', 'magazine'],
    3: ['bell', 'note'],
    4: ['brain', 'mirror', 'newspaper'],
    5: ['coat'],
    6: ['beer', 'stone'],
}

# Define the moves
moves = [
    (5, None, 'coat'),       # Remove the coat from Box 5
    (1, 2, 'knife'),         # Move the knife from Box 1 to Box 2
    (6, 5, 'stone'),         # Move the stone from Box 6 to Box 5
    (6, 3, 'beer'),          # Move the beer from Box 6 to Box 3
    (5, None, 'stone'),      # Remove the stone from Box 5
    (None, 5, 'fig'),        # Put the fig into Box 5
    (2, None, 'knife'),      # Remove the knife from Box 2
    (4, 6, 'brain'),         # Move the brain from Box 4 to Box 6
    (4, 6, 'mirror'),        # Move the mirror from Box 4 to Box 6
    (6, 4, 'brain'),         # Move the brain from Box 6 to Box 4
    (None, 1, 'wire'),       # Put the wire into Box 1
    (2, 6, 'bottle'),        # Move the bottle from Box 2 to Box 6
    (2, 6, 'magazine'),      # Move the magazine from Box 2 to Box 6
    (1, None, 'wire')        # Remove the wire from Box 1
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