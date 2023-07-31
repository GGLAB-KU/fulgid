# Initialize the boxes
boxes = {
    0: ['jacket', 'ring'],
    1: ['car', 'file', 'medicine'],
    2: ['boot', 'computer', 'machine'],
    3: [],
    4: ['pipe'],
    5: [],
    6: ['crown'],
}

# Define the moves
moves = [
    (1, None, 'medicine'),   # Remove the medicine from Box 1
    (1, None, 'car'),        # Remove the car from Box 1
    (None, 4, 'fig'),        # Put the fig into Box 4
    (6, None, 'crown'),      # Remove the crown from Box 6
    (None, 3, 'bell'),       # Put the bell into Box 3
    (None, 3, 'milk'),       # Put the milk into Box 3
    (0, 6, 'jacket'),        # Move the jacket from Box 0 to Box 6
    (0, 6, 'ring'),          # Move the ring from Box 0 to Box 6
    (3, 1, 'bell'),          # Move the bell from Box 3 to Box 1
    (3, None, 'milk'),       # Remove the milk from Box 3
    (None, 3, 'hat'),        # Put the hat into Box 3
    (None, 3, 'seed'),       # Put the seed into Box 3
    (3, 5, 'hat'),           # Move the hat from Box 3 to Box 5
    (4, None, 'fig'),        # Remove the fig from Box 4
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