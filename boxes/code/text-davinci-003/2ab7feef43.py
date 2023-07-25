# Initialize the boxes
boxes = {
    0: [],
    1: ['bottle', 'cheese', 'coffee'],
    2: ['card', 'train'],
    3: ['fig', 'tissue'],
    4: ['map', 'stone'],
    5: ['branch', 'milk', 'wheel'],
    6: ['bag', 'sheet'],
}

# Define the moves
moves = [
    (None, 3, 'apple'),       # Put the apple into Box 3
    (6, None, 'bag'),         # Remove the bag from Box 6
    (6, None, 'sheet'),       # Remove the sheet from Box 6
    (5, None, 'wheel'),       # Remove the wheel from Box 5
    (5, None, 'branch'),      # Remove the branch from Box 5
    (1, 6, 'bottle'),         # Move the bottle from Box 1 to Box 6
    (5, None, 'milk'),        # Remove the milk from Box 5
    (6, None, 'bottle'),      # Remove the bottle from Box 6
    (4, 6, 'map'),            # Move the map from Box 4 to Box 6
    (4, 6, 'stone'),          # Move the stone from Box 4 to Box 6
    (6, 0, 'map'),            # Move the map from Box 6 to Box 0
    (3, 5, 'fig'),            # Move the fig from Box 3 to Box 5
    (3, 5, 'tissue'),         # Move the tissue from Box 3 to Box 5
    (None, 6, 'boot'),        # Put the boot into Box 6
    (2, 0, 'card'),           # Move the card from Box 2 to Box 0
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