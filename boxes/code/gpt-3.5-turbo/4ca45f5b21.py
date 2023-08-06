# Initialize the boxes
boxes = {
    0: ['glass', 'television'],
    1: ['guitar', 'knife'],
    2: ['jacket'],
    3: ['drug', 'medicine'],
    4: ['bag', 'dish', 'flower'],
    5: ['note'],
    6: [],
}

# Define the moves
moves = [
    (3, 6, 'drug'),         # Move the drug from Box 3 to Box 6
    (3, 6, 'medicine'),     # Move the medicine from Box 3 to Box 6
    (None, 2, 'leaf'),      # Put the leaf into Box 2
    (1, 3, 'knife'),        # Move the knife from Box 1 to Box 3
    (0, None, 'television'), # Remove the television from Box 0
    (2, 1, 'leaf'),         # Move the leaf from Box 2 to Box 1
    (4, 3, 'dish'),         # Move the dish from Box 4 to Box 3
    (5, 0, 'note'),         # Move the note from Box 5 to Box 0
    (0, None, 'glass'),     # Remove the glass from Box 0
    (None, 3, 'plane'),     # Put the plane into Box 3
    (1, 5, 'guitar'),       # Move the guitar from Box 1 to Box 5
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