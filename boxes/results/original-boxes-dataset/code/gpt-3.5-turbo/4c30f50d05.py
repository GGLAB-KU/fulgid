# Initialize the boxes
boxes = {
    0: ['car', 'jacket', 'suit'],
    1: ['boot', 'watch'],
    2: ['chemical', 'painting'],
    3: ['brain', 'milk'],
    4: ['fan'],
    5: [],
    6: ['fish', 'ring', 'tape'],
}

# Define the moves
moves = [
    (None, 5, 'bag'),       # Put the bag into Box 5
    (4, None, 'fan'),       # Remove the fan from Box 4
    (5, 2, 'bag'),          # Move the bag from Box 5 to Box 2
    (None, 1, 'crown'),     # Put the crown into Box 1
    (None, 5, 'bus'),       # Put the bus into Box 5
    (3, None, 'brain'),     # Remove the brain from Box 3
    (3, None, 'milk'),      # Remove the milk from Box 3
    (1, 5, 'watch'),        # Move the watch from Box 1 to Box 5
    (1, 5, 'crown'),        # Move the crown from Box 1 to Box 5
    (0, None, 'car'),       # Remove the car from Box 0
    (0, None, 'jacket'),    # Remove the jacket from Box 0
    (1, None, 'boot'),      # Remove the boot from Box 1
    (2, 4, 'bag'),          # Move the bag from Box 2 to Box 4
    (2, 4, 'chemical'),     # Move the chemical from Box 2 to Box 4
    (2, 4, 'painting')      # Move the painting from Box 2 to Box 4
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