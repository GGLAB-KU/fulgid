# Initialize the boxes
boxes = {
    0: [],
    1: ['chemical', 'clock'],
    2: ['watch'],
    3: ['dress', 'plant', 'sheet'],
    4: ['document', 'fig', 'string'],
    5: [],
    6: ['gift', 'newspaper', 'tissue'],
}

# Define the moves
moves = [
    (1, None, 'clock'),     # Remove the clock from Box 1
    (None, 1, 'ice'),       # Put the ice into Box 1
    (None, 2, 'bowl'),      # Put the bowl into Box 2
    (4, None, 'document'),  # Remove the document from Box 4
    (6, None, 'gift'),      # Remove the gift from Box 6
    (6, None, 'newspaper'), # Remove the newspaper from Box 6
    (6, None, 'tissue'),    # Remove the tissue from Box 6
    (1, None, 'ice'),       # Remove the ice from Box 1
    (2, 1, 'watch'),        # Move the watch from Box 2 to Box 1
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