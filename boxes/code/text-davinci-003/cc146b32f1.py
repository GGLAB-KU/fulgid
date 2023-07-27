# Initialize the boxes
boxes = {
    0: ['chemical', 'clock'],
    1: [],
    2: [],
    3: ['dress', 'hat'],
    4: ['beer', 'letter'],
    5: ['apple', 'tape', 'ticket'],
    6: ['cup', 'picture'],
}

# Define the moves
moves = [
    (4, 2, 'letter'),   # Move the letter from Box 4 to Box 2
    (4, None, 'beer'),  # Remove the beer from Box 4
    (None, 6, 'knife')  # Put the knife into Box 6
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