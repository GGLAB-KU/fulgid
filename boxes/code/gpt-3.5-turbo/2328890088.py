# Initialize the boxes
boxes = {
    0: ['cross', 'newspaper', 'train'],
    1: ['crown'],
    2: ['bag', 'car', 'tea'],
    3: ['note'],
    4: ['bomb', 'medicine'],
    5: [],
    6: ['knife', 'letter'],
}

# Define the moves
moves = [
    (3, 4, 'note'),         # Move the note from Box 3 to Box 4
    (2, 5, 'bag'),          # Move the bag from Box 2 to Box 5
    (6, None, 'letter'),    # Remove the letter from Box 6
    (4, 5, 'note'),         # Move the note from Box 4 to Box 5
    (2, 1, 'car'),          # Move the car from Box 2 to Box 1
    (4, 3, 'medicine'),     # Move the medicine from Box 4 to Box 3
    (None, 5, 'document'),  # Put the document into Box 5
    (2, None, 'tea'),       # Remove the tea from Box 2
    (1, None, 'car'),       # Remove the car from Box 1
    (0, None, 'cross'),     # Remove the cross from Box 0
    (0, None, 'newspaper'), # Remove the newspaper from Box 0
    (1, 6, 'crown'),        # Move the crown from Box 1 to Box 6
    (None, 1, 'card')       # Put the card into Box 1
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