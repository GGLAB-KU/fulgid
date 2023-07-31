# Initialize the boxes
boxes = {
    0: ['boat', 'book', 'coffee'],
    1: [],
    2: ['ice', 'machine', 'painting'],
    3: ['jacket'],
    4: ['fan', 'mirror', 'stone'],
    5: ['card', 'coat', 'cross'],
    6: ['bill', 'wire'],
}

# Define the moves
moves = [
    (0, None, 'book'),       # Remove the book from Box 0
    (2, 3, 'machine'),       # Move the machine from Box 2 to Box 3
    (2, 3, 'painting'),      # Move the painting from Box 2 to Box 3
    (2, 6, 'ice'),           # Move the ice from Box 2 to Box 6
    (0, None, 'boat'),       # Remove the boat from Box 0
    (0, None, 'coffee'),     # Remove the coffee from Box 0
    (6, None, 'wire'),       # Remove the wire from Box 6
    (None, 0, 'meat'),       # Put the meat into Box 0
    (None, 0, 'milk'),       # Put the milk into Box 0
    (6, 1, 'bill'),          # Move the bill from Box 6 to Box 1
    (None, 2, 'ball'),       # Put the ball into Box 2
    (None, 2, 'drink'),      # Put the drink into Box 2
    (0, 6, 'milk'),          # Move the milk from Box 0 to Box 6
    (6, None, 'ice'),        # Remove the ice from Box 6
    (6, None, 'milk'),       # Remove the milk from Box 6
    (0, 1, 'meat'),          # Move the meat from Box 0 to Box 1
    (4, 6, 'fan'),           # Move the fan from Box 4 to Box 6
    (4, 6, 'stone')          # Move the stone from Box 4 to Box 6
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