# Initialize the boxes
boxes = {
    0: ['boot'],
    1: ['chemical', 'creature'],
    2: ['hat'],
    3: ['knife', 'suit', 'tape'],
    4: ['beer', 'fig'],
    5: ['bell', 'disk', 'ticket'],
    6: ['picture', 'radio'],
}

# Define the moves
moves = [
    (4, None, 'beer'),       # Remove the beer from Box 4
    (4, None, 'fig'),        # Remove the fig from Box 4
    (0, 1, 'boot'),          # Move the boot from Box 0 to Box 1
    (1, None, 'boot'),       # Remove the boot from Box 1
    (1, None, 'chemical'),   # Remove the chemical from Box 1
    (None, 0, 'book'),       # Put the book into Box 0
    (None, 0, 'branch')      # Put the branch into Box 0
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