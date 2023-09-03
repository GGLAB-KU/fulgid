# Initialize the boxes
boxes = {
    0: ['game', 'hat'],
    1: ['car', 'creature', 'plane'],
    2: [],
    3: ['egg'],
    4: ['dish'],
    5: ['key', 'ring', 'tissue'],
    6: ['drink', 'milk', 'note'],
}

# Define the moves
moves = [
    (3, None, 'egg'),       # Remove the egg from Box 3
    (None, 2, 'cross'),     # Put the cross into Box 2
    (None, 2, 'glass'),     # Put the glass into Box 2
    (1, 4, 'car'),          # Move the car from Box 1 to Box 4
    (0, None, 'hat'),       # Remove the hat from Box 0
    (0, 3, 'game'),         # Move the game from Box 0 to Box 3
    (5, None, 'ring'),      # Remove the ring from Box 5
    (5, None, 'tissue'),    # Remove the tissue from Box 5
    (1, None, 'creature'),  # Remove the creature from Box 1
    (3, 5, 'game'),         # Move the game from Box 3 to Box 5
    (4, 0, 'car'),          # Move the car from Box 4 to Box 0
    (4, 0, 'dish'),         # Move the dish from Box 4 to Box 0
    (6, 4, 'milk'),         # Move the milk from Box 6 to Box 4
    (6, 4, 'note'),         # Move the note from Box 6 to Box 4
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