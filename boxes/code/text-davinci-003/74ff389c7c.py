# Initialize the boxes
boxes = {
    0: [],
    1: ['plane', 'pot', 'sheet'],
    2: ['cup', 'tissue'],
    3: ['dish', 'guitar', 'plate'],
    4: ['gift', 'plant', 'shell'],
    5: ['book', 'cake', 'paper'],
    6: ['ice'],
}

# Define the moves
moves = [
    (None, 0, 'car'),       # Put the car into Box 0
    (None, 6, 'cheese'),    # Put the cheese into Box 6
    (5, None, 'book'),      # Remove the book from Box 5
    (5, None, 'paper'),     # Remove the paper from Box 5
    (0, 5, 'car'),          # Move the car from Box 0 to Box 5
    (None, 0, 'coffee'),    # Put the coffee into Box 0
    (6, 5, 'ice'),          # Move the ice from Box 6 to Box 5
    (3, None, 'guitar'),    # Remove the guitar from Box 3
    (3, None, 'plate'),     # Remove the plate from Box 3
    (5, None, 'cake'),      # Remove the cake from Box 5
    (5, None, 'bomb'),      # Put the bomb into Box 5
    (5, 2, 'car'),          # Move the car from Box 5 to Box 2
    (None, 6, 'wire')       # Put the wire into Box 6
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