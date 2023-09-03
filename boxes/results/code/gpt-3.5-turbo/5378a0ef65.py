# Initialize the boxes
boxes = {
    0: ['fan', 'flower', 'game'],
    1: ['ball', 'glass', 'tissue'],
    2: ['suit'],
    3: ['cake', 'rose', 'train'],
    4: ['apple', 'disk', 'dress'],
    5: ['beer', 'plate'],
    6: ['gift', 'key', 'stone'],
}

# Define the moves
moves = [
    (3, None, 'cake'),       # Remove the cake from Box 3
    (3, None, 'train'),      # Remove the train from Box 3
    (1, None, 'ball'),       # Remove the ball from Box 1
    (1, None, 'tissue'),     # Remove the tissue from Box 1
    (5, None, 'beer'),       # Remove the beer from Box 5
    (None, 2, 'coat'),       # Put the coat into Box 2
    (None, 2, 'letter'),     # Put the letter into Box 2
    (3, None, 'rose'),       # Remove the rose from Box 3
    (6, None, 'stone'),      # Remove the stone from Box 6
    (4, None, 'disk'),       # Remove the disk from Box 4
    (4, None, 'dress')       # Remove the dress from Box 4
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