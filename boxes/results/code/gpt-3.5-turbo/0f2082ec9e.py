# Initialize the boxes
boxes = {
    0: ['beer', 'file'],
    1: ['computer'],
    2: ['hat', 'tape'],
    3: ['block', 'meat'],
    4: ['guitar', 'map', 'tissue'],
    5: ['fan', 'suit', 'ticket'],
    6: ['jacket'],
}

# Define the moves
moves = [
    (None, 0, 'bomb'),       # Put the bomb into Box 0
    (5, None, 'suit'),       # Remove the suit from Box 5
    (5, None, 'ticket')      # Remove the ticket from Box 5
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