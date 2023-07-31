# Initialize the boxes
boxes = {
    0: ['camera', 'phone', 'shirt'],
    1: ['game', 'ice'],
    2: [],
    3: ['painting'],
    4: ['bottle', 'computer', 'tape'],
    5: ['drug'],
    6: ['shell', 'shoe'],
}

# Define the moves
moves = [
    (1, 5, 'ice'),          # Move the ice from Box 1 to Box 5
    (None, 3, 'brain'),     # Put the brain into Box 3
    (4, None, 'computer'),  # Remove the computer from Box 4
    (4, None, 'tape'),      # Remove the tape from Box 4
    (None, 1, 'paper'),     # Put the paper into Box 1
    (5, 1, 'ice'),          # Move the ice from Box 5 to Box 1
    (3, None, 'brain'),     # Remove the brain from Box 3
    (0, None, 'camera'),    # Remove the camera from Box 0
    (0, None, 'phone'),     # Remove the phone from Box 0
    (0, None, 'shirt'),     # Remove the shirt from Box 0
    (5, None, 'drug'),      # Remove the drug from Box 5
    (None, 0, 'chemical'),  # Put the chemical into Box 0
    (None, 0, 'seed'),      # Put the seed into Box 0
    (None, 3, 'rose'),      # Put the rose into Box 3
    (None, 5, 'bomb'),      # Put the bomb into Box 5
    (None, 5, 'milk'),      # Put the milk into Box 5
    (4, 5, 'bottle'),       # Move the bottle from Box 4 to Box 5
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