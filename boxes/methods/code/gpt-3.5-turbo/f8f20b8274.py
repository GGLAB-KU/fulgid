# Initialize the boxes
boxes = {
    0: ['cream', 'painting'],
    1: ['apple', 'bag', 'milk'],
    2: ['drink', 'sheet'],
    3: ['plane'],
    4: ['phone'],
    5: ['meat', 'note'],
    6: ['branch', 'document', 'tea'],
}

# Define the moves
moves = [
    (None, 4, 'bowl'),       # Put the bowl into Box 4
    (None, 4, 'key'),        # Put the key into Box 4
    (6, 5, 'branch'),        # Move the branch from Box 6 to Box 5
    (0, None, 'painting'),   # Remove the painting from Box 0
    (None, 0, 'tape'),       # Put the tape into Box 0
    (2, 3, 'drink'),         # Move the drink from Box 2 to Box 3
    (2, 3, 'sheet'),         # Move the sheet from Box 2 to Box 3
    (6, 2, 'tea'),           # Move the tea from Box 6 to Box 2
    (1, None, 'apple'),      # Remove the apple from Box 1
    (1, None, 'bag'),        # Remove the bag from Box 1
    (0, None, 'brain'),      # Put the brain into Box 0
    (4, 6, 'phone'),         # Move the phone from Box 4 to Box 6
    (4, None, 'key'),        # Remove the key from Box 4
    (1, 6, 'milk'),          # Move the milk from Box 1 to Box 6
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