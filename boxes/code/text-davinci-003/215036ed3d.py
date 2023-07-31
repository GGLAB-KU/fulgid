# Initialize the boxes
boxes = {
    0: ['disk'],
    1: ['ball', 'crown'],
    2: ['shirt'],
    3: [],
    4: ['bottle', 'egg', 'leaf'],
    5: ['block', 'engine', 'plane'],
    6: ['bomb', 'flower'],
}

# Define the moves
moves = [
    (2, 1, 'shirt'),        # Move the shirt from Box 2 to Box 1
    (6, None, 'bomb'),      # Remove the bomb from Box 6
    (6, None, 'flower'),    # Remove the flower from Box 6
    (None, 2, 'car'),       # Put the car into Box 2
    (None, 2, 'game'),      # Put the game into Box 2
    (None, 0, 'letter'),    # Put the letter into Box 0
    (4, None, 'bottle'),    # Remove the bottle from Box 4
    (4, None, 'egg'),       # Remove the egg from Box 4
    (4, None, 'leaf'),      # Remove the leaf from Box 4
    (None, 4, 'bag'),       # Put the bag into Box 4
    (None, 4, 'magazine'),  # Put the magazine into Box 4
    (2, None, 'car'),       # Remove the car from Box 2
    (2, None, 'game'),      # Remove the game from Box 2
    (0, 6, 'disk'),         # Move the disk from Box 0 to Box 6
    (0, 6, 'letter'),       # Move the letter from Box 0 to Box 6
    (None, 4, 'seed'),      # Put the seed into Box 4
    (None, 0, 'rock'),      # Put the rock into Box 0
    (6, None, 'letter'),    # Remove the letter from Box 6
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