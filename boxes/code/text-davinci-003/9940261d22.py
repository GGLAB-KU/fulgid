# Initialize the boxes
boxes = {
    0: ['bread', 'leaf'],
    1: [],
    2: [],
    3: ['apple', 'cash'],
    4: ['bag', 'chemical', 'tape'],
    5: [],
    6: ['beer', 'cigarette', 'shell'],
}

# Define the moves
moves = [
    (4, 5, 'bag'),          # Move the bag from Box 4 to Box 5
    (4, 5, 'chemical'),     # Move the chemical from Box 4 to Box 5
    (4, 5, 'tape'),         # Move the tape from Box 4 to Box 5
    (None, 3, 'drug'),      # Put the drug into Box 3
    (None, 2, 'drink'),     # Put the drink into Box 2
    (None, 0, 'milk'),      # Put the milk into Box 0
    (6, None, 'cigarette'), # Remove the cigarette from Box 6
    (6, None, 'shell'),     # Remove the shell from Box 6
    (None, 2, 'boot'),      # Put the boot into Box 2
    (None, 2, 'rose'),      # Put the rose into Box 2
    (5, 6, 'bag'),          # Move the bag from Box 5 to Box 6
    (5, 6, 'tape'),         # Move the tape from Box 5 to Box 6
    (3, None, 'drug'),      # Remove the drug from Box 3
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