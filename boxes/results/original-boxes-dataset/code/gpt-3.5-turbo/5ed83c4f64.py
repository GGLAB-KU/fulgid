# Initialize the boxes
boxes = {
    0: ['cigarette', 'crown'],
    1: ['medicine', 'plate'],
    2: ['cup', 'disk', 'note'],
    3: ['document', 'egg'],
    4: ['bell', 'drug'],
    5: [],
    6: ['phone', 'rock'],
}

# Define the moves
moves = [
    (3, 4, 'egg'),          # Move the egg from Box 3 to Box 4
    (1, 3, 'medicine'),     # Move the medicine from Box 1 to Box 3
    (1, 3, 'plate'),        # Move the plate from Box 1 to Box 3
    (None, 1, 'bag'),       # Put the bag into Box 1
    (None, 1, 'ring'),      # Put the ring into Box 1
    (None, 1, 'tissue'),    # Put the tissue into Box 1
    (1, None, 'ring'),      # Remove the ring from Box 1
    (2, None, 'cup'),       # Remove the cup from Box 2
    (2, None, 'disk'),      # Remove the disk from Box 2
    (2, 5, 'note'),         # Move the note from Box 2 to Box 5
    (5, None, 'note'),      # Remove the note from Box 5
    (6, 5, 'rock'),         # Move the rock from Box 6 to Box 5
    (5, 0, 'rock'),         # Move the rock from Box 5 to Box 0
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