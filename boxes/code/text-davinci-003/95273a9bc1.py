# Initialize the boxes
boxes = {
    0: ['key', 'magazine'],
    1: ['shell'],
    2: ['fan', 'plate'],
    3: ['medicine'],
    4: ['book', 'cash', 'coffee'],
    5: ['beer', 'game'],
    6: ['file'],
}

# Define the moves
moves = [
    (5, 6, 'beer'),         # Move the beer from Box 5 to Box 6
    (5, 6, 'game'),         # Move the game from Box 5 to Box 6
    (4, 3, 'book'),         # Move the book from Box 4 to Box 3
    (4, 3, 'coffee'),       # Move the coffee from Box 4 to Box 3
    (2, None, 'plate'),     # Remove the plate from Box 2
    (4, None, 'cash'),      # Remove the cash from Box 4
    (1, None, 'shell'),     # Remove the shell from Box 1
    (3, 2, 'coffee'),       # Move the coffee from Box 3 to Box 2
    (None, 5, 'boot'),      # Put the boot into Box 5
    (3, None, 'book'),      # Remove the book from Box 3
    (5, 4, 'boot'),         # Move the boot from Box 5 to Box 4
    (0, None, 'magazine')   # Remove the magazine from Box 0
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