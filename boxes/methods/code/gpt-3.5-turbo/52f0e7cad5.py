# Initialize the boxes
boxes = {
    0: ['shell'],
    1: [],
    2: ['dish', 'letter', 'plant'],
    3: ['cake', 'machine', 'note'],
    4: ['block', 'drink', 'flower'],
    5: ['gift'],
    6: ['cheese', 'ice', 'train'],
}

# Define the moves
moves = [
    (5, None, 'gift'),       # Remove the gift from Box 5
    (4, None, 'drink'),      # Remove the drink from Box 4
    (2, 1, 'dish'),          # Move the dish from Box 2 to Box 1
    (4, None, 'block'),      # Remove the block from Box 4
    (3, 5, 'cake'),          # Move the cake from Box 3 to Box 5
    (3, 5, 'machine'),       # Move the machine from Box 3 to Box 5
    (3, 5, 'note'),          # Move the note from Box 3 to Box 5
    (4, 0, 'flower'),        # Move the flower from Box 4 to Box 0
    (2, None, 'letter'),     # Remove the letter from Box 2
    (5, None, 'machine'),    # Remove the machine from Box 5
    (5, None, 'note'),       # Remove the note from Box 5
    (0, 5, 'flower'),        # Move the flower from Box 0 to Box 5
    (0, 5, 'shell'),         # Move the shell from Box 0 to Box 5
    (5, 0, 'cake'),          # Move the cake from Box 5 to Box 0
    (5, 0, 'flower'),        # Move the flower from Box 5 to Box 0
    (5, 4, 'shell'),         # Move the shell from Box 5 to Box 4
    (6, None, 'cheese'),     # Remove the cheese from Box 6
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