# Initialize the boxes
boxes = {
    0: ['rock'],
    1: ['block', 'dish'],
    2: ['drink', 'hat', 'shirt'],
    3: ['boot', 'fig', 'medicine'],
    4: ['coat', 'egg', 'flower'],
    5: ['disk', 'phone'],
    6: [],
}

# Define the moves
moves = [
    (0, 6, 'rock'),         # Move the rock from Box 0 to Box 6
    (5, None, 'disk'),      # Remove the disk from Box 5
    (5, None, 'phone'),     # Remove the phone from Box 5
    (2, 5, 'drink'),        # Move the drink from Box 2 to Box 5
    (2, 5, 'hat'),          # Move the hat from Box 2 to Box 5
    (4, 6, 'egg'),          # Move the egg from Box 4 to Box 6
    (4, 6, 'flower'),       # Move the flower from Box 4 to Box 6
    (2, 0, 'shirt'),        # Move the shirt from Box 2 to Box 0
    (5, 1, 'hat'),          # Move the hat from Box 5 to Box 1
    (1, None, 'dish'),      # Remove the dish from Box 1
    (1, None, 'hat'),       # Remove the hat from Box 1
    (0, None, 'shirt')      # Remove the shirt from Box 0
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